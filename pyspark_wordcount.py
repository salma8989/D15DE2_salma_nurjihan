# -*- coding: utf-8 -*-
"""pyspark_wordcount.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QURU2Svxv9HBZYUhNApskwTsX4VXJ55c
"""

# Create SparkSession and sparkcontext
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('wordcountPyspark').getOrCreate()
sc=spark.sparkContext


# Read the input file and Calculating words count
text_file = sc.textFile("gs://pub/shakespeare/rose.txt")
counts = text_file.flatMap(lambda line: line.split(" "))\
                            .map(lambda word: (word, 1))\
                           .reduceByKey(lambda x, y: x + y)


# Printing each word with its respective count
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))


# Stopping Spark-Session and Spark context
sc.stop()
spark.stop()