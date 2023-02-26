import sqlite3
from statistics import mean, stdev,median
from scipy.stats import f_oneway,kruskal,tukey_hsd,shapiro, levene
import numpy as np
import csv

#import pingouin as pg
#import pandas as pd

dbStaticConnection = sqlite3.connect("./rawData/fantasizefreelyStatic/dbStatic.sqlite")
dbBasicConnection = sqlite3.connect("./rawData/fantasizefreelyBasic/dbBasic.sqlite")
dbConnection = sqlite3.connect("./rawData/fantasizefreely/db.sqlite")

static_cur = dbStaticConnection.cursor()
basic_cur = dbBasicConnection.cursor()
cur = dbConnection.cursor()


"""res = cur.execute("SELECT * FROM Scores")
result = res.fetchall()
with open('InspirationScores.csv', 'w', encoding='utf-8') as inspiration:
    writer = csv.writer(inspiration, delimiter=',')
    for elem in result:

        resCompositions = cur.execute("SELECT * FROM compositions WHERE id = ?", [elem[1]])
        resultCompositions = resCompositions.fetchall()
        composition = resultCompositions[0]
        subject = composition[1]


        row=[]
        row.append(elem[0])
        row.append(elem[1])
        row.append(elem[2])
        row.append(elem[3])
        row.append(elem[4])


        writer.writerow([subject]+row)"""


"""
res = basic_cur.execute("SELECT * FROM Scores")
result = res.fetchall()
with open('BasicScores.csv', 'w', encoding='utf-8') as inspiration:
    writer = csv.writer(inspiration, delimiter=',')
    for elem in result:
        resCompositions = basic_cur.execute("SELECT * FROM compositions WHERE id = ?", [elem[1]])
        resultCompositions = resCompositions.fetchall()
        composition = resultCompositions[0]
        subject = composition[1]


        row=[]
        row.append(elem[0])
        row.append(elem[1])
        row.append(elem[2])
        row.append(elem[3])
        row.append(elem[4])


        writer.writerow([subject]+row) """


res = static_cur.execute("SELECT * FROM Scores")
result = res.fetchall()
with open('StaticScores.csv', 'w', encoding='utf-8') as inspiration:
    writer = csv.writer(inspiration, delimiter=',')
    for elem in result:
        resCompositions = static_cur.execute("SELECT * FROM compositions WHERE id = ?", [elem[1]])
        resultCompositions = resCompositions.fetchall()
        composition = resultCompositions[0]
        subject = composition[1]


        row=[]
        row.append(elem[0])
        row.append(elem[1])
        row.append(elem[2])
        row.append(elem[3])
        row.append(elem[4])


        writer.writerow([subject]+row)








"""resStatic = static_cur.execute("SELECT * FROM Scores")
resultStatic = resStatic.fetchall()
print(resultStatic)

resBasic = basic_cur.execute("SELECT * FROM Scores")
resultBasic = resBasic.fetchall()
print(resultBasic)"""




