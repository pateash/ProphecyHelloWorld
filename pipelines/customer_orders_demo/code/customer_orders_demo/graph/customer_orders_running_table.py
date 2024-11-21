from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders_demo.config.ConfigStore import *
from customer_orders_demo.functions import *

def customer_orders_running_table(spark: SparkSession, WindowFunction_1: DataFrame):
    WindowFunction_1.write\
        .format("delta")\
        .option("mergeSchema", True)\
        .mode("overwrite")\
        .saveAsTable("`prophecy_demos`.`customer_orders_running_table`")
