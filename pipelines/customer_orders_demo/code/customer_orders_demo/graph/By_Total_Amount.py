from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders_demo.config.ConfigStore import *
from customer_orders_demo.functions import *

def By_Total_Amount(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("amounts").desc())
