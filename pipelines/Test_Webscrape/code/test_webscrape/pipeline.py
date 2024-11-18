from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from test_webscrape.config.ConfigStore import *
from test_webscrape.udfs.UDFs import *
from prophecy.utils import *
from test_webscrape.graph import *

def pipeline(spark: SparkSession) -> None:
    df_poloniex_data = poloniex_data(spark)
    df_parse_response = parse_response(spark, df_poloniex_data)
    df_convert_timestamps = convert_timestamps(spark, df_parse_response)
    write_delta_table(spark, df_convert_timestamps)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Test_Webscrape")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Test_Webscrape", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Test_Webscrape")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
