

from __future__ import print_function
from pandas import read_csv
from mysql import connector
import itertools
import string
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from decimal import *
from cubes import workspace

print("preparing data...")


mydb = connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="olapdb"
)

mycursor = mydb.cursor()

Q = """SELECT country,Big.gold_sum/Big.co,Big.silver_sum/Big.co,Big.bronze_sum/Big.co,Big.s/Big.co as r
            FROM (SELECTcountry,sum(gold)as gold_sum,sum(silver)as silver_sum,SUM(bronze)as bronze_sum,COUNT(*) as co,sum(gold+silver+bronze)as s
                      FROM london12
                      GROUP BY country
                      HAVING count(*) >=30 ) as Big
            ORDER BY r
            DESC LIMIT 10 """
mycursor.execute(Q)
records = mycursor.fetchall()
array1 = []
array2 = []
array3 = []
array4 = []
# print(records)
for row in records:
    array1.append(row[0])
    array2.append(row[1])
    array3.append(row[2])
    array4.append(row[3])
ax = plt.subplot(111)
ax.bar(array1, array2, width=0.5, color='b', align='center')
ax.bar(array1, array3, width=0.5, color='g', align='center')
ax.bar(array1, array4, width=0.5, color='r', align='center')
plt.show()
