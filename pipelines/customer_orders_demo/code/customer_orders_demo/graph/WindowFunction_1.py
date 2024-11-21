from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders_demo.config.ConfigStore import *
from customer_orders_demo.functions import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn(
        "order_amount_running_total",
        sum(col("amount"))\
          .over(Window\
          .partitionBy(col("customer_id"))\
          .orderBy(col("order_id").asc())\
          .rowsBetween(Window.unboundedPreceding, Window.currentRow))
    )
