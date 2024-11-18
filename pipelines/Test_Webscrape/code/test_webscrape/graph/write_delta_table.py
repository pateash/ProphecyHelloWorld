from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_webscrape.config.ConfigStore import *
from test_webscrape.udfs.UDFs import *

def write_delta_table(spark: SparkSession, in0: DataFrame):
    from delta.tables import DeltaTable, DeltaMergeBuilder

    if (
        DeltaTable.isDeltaTable(spark, "dbfs:/webscrape-demo/poloniex/BTC_USDT/")
        and spark._jvm.org.apache.hadoop.fs.FileSystem\
          .get(spark._jsc.hadoopConfiguration())\
          .exists(spark._jvm.org.apache.hadoop.fs.Path("dbfs:/webscrape-demo/poloniex/BTC_USDT/"))
    ):
        DeltaTable\
            .forPath(spark, "dbfs:/webscrape-demo/poloniex/BTC_USDT/")\
            .alias("target")\
            .merge(in0.alias("source"), (col("source.id") == col("target.id")))\
            .whenMatchedUpdateAll()\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write\
            .format("delta")\
            .option("mergeSchema", False)\
            .mode("overwrite")\
            .save("dbfs:/webscrape-demo/poloniex/BTC_USDT/")
