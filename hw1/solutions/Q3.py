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

mydb = connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="olapdb"
)

mycursor = mydb.cursor()

################## Question 3 #########################

strings = ["sport","agegroup","gender","country","continent"]

def convertTuple(tup):
    str =  ','.join(tup)
    return str
k = 0;
for i in range(1,5):
    sList = list(itertools.combinations(strings, i))
    for j in range(0,len(sList)):
        # print(convertTuple(sList.__getitem__(j)))
        s = """CREATE INDEX h"""+str(k)+""" ON london12(""" + convertTuple(sList.__getitem__(j)) + """);"""
        k+=1
        print(s)
        mycursor.execute(s)