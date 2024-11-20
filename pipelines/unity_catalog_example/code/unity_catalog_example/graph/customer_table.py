from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unity_catalog_example.config.ConfigStore import *
from unity_catalog_example.functions import *

def customer_table(spark: SparkSession) -> DataFrame:
    return spark.read.table("`prophecy_demos`.`customers`")
