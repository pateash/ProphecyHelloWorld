from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders_demo.config.ConfigStore import *
from customer_orders_demo.functions import *

def customers_orders_table(spark: SparkSession, Sum_Amounts: DataFrame):
    Sum_Amounts.write\
        .format("delta")\
        .option("mergeSchema", True)\
        .mode("overwrite")\
        .saveAsTable("`prophecy_demos`.`customer_orders_table`")
