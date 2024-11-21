from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders_demo.config.ConfigStore import *
from customer_orders_demo.functions import *

def inr_amount(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        (col("amounts") * lit(84.6)).alias("amounts"), 
        col("customer_id"), 
        col("orders"), 
        col("account_length_days"), 
        col("first_name"), 
        col("last_name")
    )
