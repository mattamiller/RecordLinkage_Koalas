# Databricks notebook source
import databricks.koalas as ks

df = ks.DataFrame({'x': [1, 2], 'y': [3, 4], 'z': [5, 6]})
# Rename columns
df.columns = ['x', 'y','z1']
# Do some operations in place
df['x2'] = df.x * df.x

# COMMAND ----------

