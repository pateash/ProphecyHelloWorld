from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_webscrape.config.ConfigStore import *
from test_webscrape.udfs.UDFs import *

def parse_response(spark: SparkSession, in0: DataFrame) -> DataFrame:
    column_data = in0.withColumn("json_content", decode(col("content"), 'utf-8'))
    json_line_schema = StructType([
        StructField("id", IntegerType()),
        StructField("price", DecimalType(12.4)),
        StructField("quantity", DecimalType(12.4)),
        StructField("amount", DecimalType(12.4)),
        StructField("takerSide", StringType()),
        StructField("ts", DoubleType()),
        StructField("createTime", DoubleType())
    ])
    json_doc_schema = ArrayType(StringType())
    df = column_data\
             .withColumn("converted_json", from_json("json_content", json_doc_schema))\
             .withColumn("exploded_data", explode("converted_json"))\
             .withColumn("data", from_json("exploded_data", json_line_schema))\
             .select("data")
    out0 = df.select(
        df.data.id,
        df.data.price,
        df.data.quantity,
        df.data.amount,
        df.data.takerSide,
        df.data.ts,
        df.data.createTime
    )

    return out0
