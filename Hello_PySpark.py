from pyspark.sql import SparkSession
import findspark


findspark.init()

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

myRDD = sc.paralleize([100, 200, 300, 400, 500])

print(myRDD.take(3))
