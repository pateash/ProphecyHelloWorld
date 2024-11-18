from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_webscrape.config.ConfigStore import *
from test_webscrape.udfs.UDFs import *

def poloniex_data(spark: SparkSession) -> DataFrame:
    from spark_ai.webapps import WebUtils
    WebUtils().register_udfs(spark)
    df1 = spark.range(1)

    return df1\
        .withColumn("url", lit("https://api.poloniex.com/markets/BTC_USDT/trades?limit=1000"))\
        .withColumn("content", expr("web_scrape(url)"))
