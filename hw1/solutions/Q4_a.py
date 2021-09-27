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
################## Question 4 , part a #########################

query = """SELECT country,COUNT(*)
FROM london12
GROUP BY country
ORDER BY COUNT(*)
DESC LIMIT 10
;"""

mycursor.execute(query)
records = mycursor.fetchall()

s1 = []
s2 = []

for row in records:
    s1.append(row[0])
    s2.append(row[1])

df = pd.DataFrame({'country':s1, 'number of participants':s2})
ax = df.plot.bar(x='country', y='number of participants', rot=0)
plt.show()