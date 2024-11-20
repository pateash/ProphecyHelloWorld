from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from unity_catalog_example.config.ConfigStore import *
from unity_catalog_example.functions import *
from prophecy.utils import *
from unity_catalog_example.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customer_table = customer_table(spark)
    df_orders_table = orders_table(spark)
    df_By_CustomerId = By_CustomerId(spark, df_customer_table, df_orders_table)
    df_Cleanup = Cleanup(spark, df_By_CustomerId)
    df_Sum_Amounts = Sum_Amounts(spark, df_Cleanup)
    customers_orders(spark, df_Sum_Amounts)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("unity_catalog_example")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/unity_catalog_example")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/unity_catalog_example", config = Config)(pipeline)

if __name__ == "__main__":
    main()
