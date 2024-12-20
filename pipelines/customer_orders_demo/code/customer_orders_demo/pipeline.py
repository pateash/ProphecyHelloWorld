from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customer_orders_demo.config.ConfigStore import *
from customer_orders_demo.functions import *
from prophecy.utils import *
from customer_orders_demo.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customer_table = customer_table(spark)
    df_orders_table = orders_table(spark)
    df_By_CustomerId = By_CustomerId(spark, df_customer_table, df_orders_table)
    df_Cleanup = Cleanup(spark, df_By_CustomerId)
    df_Sum_Amounts = Sum_Amounts(spark, df_Cleanup)
    df_inr_amount = inr_amount(spark, df_Sum_Amounts)
    df_add_full_name = add_full_name(spark, df_inr_amount)
    df_customers_orders_table_source = customers_orders_table_source(spark)
    customers_orders_table(spark, df_add_full_name)
    df_By_Total_Amount = By_Total_Amount(spark, df_customers_orders_table_source)
    df_Top_10 = Top_10(spark, df_By_Total_Amount)
    report_table(spark, df_Top_10)
    df_WindowFunction_1 = WindowFunction_1(spark, df_Cleanup)
    customer_orders_running_table(spark, df_WindowFunction_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("customer_orders_demo")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customer_orders_demo")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/customer_orders_demo", config = Config)(pipeline)

if __name__ == "__main__":
    main()
