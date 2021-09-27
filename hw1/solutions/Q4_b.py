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


##############################  Q4 , part b ###########################################
query2 = """ SELECT continent, (SUM(gold)+SUM(silver)+SUM(bronze))
FROM london12
GROUP BY continent ;
"""

mycursor.execute(query2)
records2= mycursor.fetchall()

r1 = []
r2 = []

for row in records2:
    r1.append(row[0])
    r2.append(row[1])

df2 = pd.DataFrame(records2,columns=['r1','r2'])
plt.pie(df2['r2'],labels=df2['r1'],autopct="%.2f")

plt.show()