# -*- coding: utf-8 -*-
# Data preparation for the hello_world example
from __future__ import print_function
from mysql import connector
from pandas import read_csv


# 1. Prepare SQL data in memory

print("preparing data...")

mydb = connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="olapdb"
)

df = read_csv('data.csv')

mycursor = mydb.cursor()

for index, row in df.iterrows():
    sql = "INSERT INTO irbd_balance VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (row["Category Code"], row["Category"], row["Subcategory Code"], row["Subcategory"],
           row["Line Item"], row["Fiscal Year"], row["Amount (US$, Millions)"])
    mycursor.execute(sql, val)


mydb.commit()

print("done. file data.sqlite created")
