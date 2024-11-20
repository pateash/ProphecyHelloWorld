from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unity_catalog_example.config.ConfigStore import *
from unity_catalog_example.functions import *

def customers_orders(spark: SparkSession, Sum_Amounts: DataFrame):
    Sum_Amounts.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable("`prophecy_ashish_dev_cloud`.`customer_orders_table`")
