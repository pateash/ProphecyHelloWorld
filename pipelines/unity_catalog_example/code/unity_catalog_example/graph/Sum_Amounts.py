from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unity_catalog_example.config.ConfigStore import *
from unity_catalog_example.functions import *

def Sum_Amounts(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("customer_id"))

    return df1.agg(
        count(col("order_id")).alias("orders"), 
        (sum(col("amount")) + lit(2)).alias("amounts"), 
        first(col("account_length_days")).alias("account_length_days")
    )
