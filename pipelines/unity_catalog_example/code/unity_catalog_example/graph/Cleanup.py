from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unity_catalog_example.config.ConfigStore import *
from unity_catalog_example.functions import *

def Cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        datediff(current_date(), col("account_open_date")).alias("account_length_days"), 
        col("order_id"), 
        col("customer_id"), 
        col("amount")
    )
