from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_webscrape.config.ConfigStore import *
from test_webscrape.udfs.UDFs import *

def convert_timestamps(spark: SparkSession, Script_1: DataFrame) -> DataFrame:
    return Script_1.select(
        from_unixtime((col("`data.ts`") / lit(1000))).alias("data.ts"), 
        from_unixtime((col("`data.createTime`") / lit(1000))).alias("data.createTime")
    )
