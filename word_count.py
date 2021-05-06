import pyspark

import findspark


findspark.init()

sc=pyspark.SparkContext("local[*]")

txt =sc.textFile('C:/Spark/spark-3.0.2-bin-hadoop2.7/bin/test.txt')

print(txt.count())

python_lines=txt.filter(lambda line :'apache' in line.lower())

print(python_lines)