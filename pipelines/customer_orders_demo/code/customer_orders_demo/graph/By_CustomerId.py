from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders_demo.config.ConfigStore import *
from customer_orders_demo.functions import *

def By_CustomerId(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.customer_id") == col("in1.customer_id")), "inner")\
        .select(col("in0.account_open_date").alias("account_open_date"), col("in1.order_id").alias("order_id"), col("in1.customer_id").alias("customer_id"), col("in1.amount").alias("amount"), col("in0.first_name").alias("first_name"), col("in0.last_name").alias("last_name"))
