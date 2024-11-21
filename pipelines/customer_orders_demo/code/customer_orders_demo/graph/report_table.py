from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders_demo.config.ConfigStore import *
from customer_orders_demo.functions import *

def report_table(spark: SparkSession, Top_10: DataFrame):
    Top_10.write.format("delta").mode("overwrite").saveAsTable("`prophecy_demos`.`report_table`")
