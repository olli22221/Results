import sqlite3
from statistics import mean, stdev,median
from scipy.stats import f_oneway,kruskal,tukey_hsd,shapiro, levene
import numpy as np

#import pingouin as pg
#import pandas as pd

dbStaticConnection = sqlite3.connect("../ExperimentData/fantasizefreelyStatic/dbStatic.sqlite")
dbBasicConnection = sqlite3.connect("../ExperimentData/fantasizefreelyBasic/dbBasic.sqlite")
dbConnection = sqlite3.connect("../ExperimentData/fantasizefreely/db.sqlite")

static_cur = dbStaticConnection.cursor()
basic_cur = dbBasicConnection.cursor()
cur = dbConnection.cursor()


res = cur.execute("SELECT * FROM Scores")
result = res.fetchall()

resStatic = static_cur.execute("SELECT * FROM Scores")
resultStatic = resStatic.fetchall()

resBasic = basic_cur.execute("SELECT * FROM Scores")
resultBasic = resBasic.fetchall()

staticFluency = []
basicFluency = []
Fluency = []

staticFlexability = []
basicFlexability = []
Flexability = []

staticOriginality = []
basicOriginality = []
Originality = []


for elem in result:
    Fluency.append(elem[2])
    Flexability.append(elem[3])
    Originality.append(elem[4])

for elem in resultBasic:
    basicFluency.append(elem[2])
    basicFlexability.append(elem[3])
    basicOriginality.append(elem[4])

for elem in resultStatic:
    staticFluency.append(elem[2])
    staticFlexability.append(elem[3])
    staticOriginality.append(elem[4])


staticFluencyMean = mean(staticFluency)
basicFluencyMean = mean(basicFluency)
FluencyMean = mean(Fluency)

staticFlexabilityMean = mean(staticFlexability)
basicFlexabilityMean = mean(basicFlexability)
FlexabilityMean = mean(Flexability)

staticOriginalityMean = mean(staticOriginality)
basicOriginalityMean = mean(basicOriginality)
OriginalityMean = mean(Originality)

staticFluencySD = 0
basicFluencySD = 0
FluencyMeanSD = 0

# unbedingt noch besondere Kompositionen hervorheben und als mp3 oder wav vorführen.


print("Mean Scores Static     Basic      Inspiration:\n")
print("Fluency: " + str(staticFluencyMean) + "  " + str(basicFluencyMean) + "  " + str(FluencyMean)+"\n")
print("Flexability: " + str(staticFlexabilityMean) + "  " + str(basicFlexabilityMean) + "  " + str(FlexabilityMean)+"\n")
print("Originality: " + str(staticOriginalityMean) + "  " + str(basicOriginalityMean) + "  " + str(OriginalityMean)+"\n")

print("Std Scores Static     Basic      Inspiration:\n")
print("Fluency: " + str(stdev(staticFluency)) + "  " + str(stdev(basicFluency)) + "  " + str(stdev(Fluency))+"\n")
print("Flexability: " + str(stdev(staticFlexability)) + "  " + str(stdev(basicFlexability)) + "  " + str(stdev(Flexability))+"\n")
print("Originality: " + str(stdev(staticOriginality)) + "  " + str(stdev(basicOriginality)) + "  " + str(stdev(Originality))+"\n")

print("Mdn Scores Static     Basic      Inspiration:\n")
print("Fluency: " + str(median(staticFluency)) + "  " + str(median(basicFluency)) + "  " + str(median(Fluency))+"\n")
print("Flexability: " + str(median(staticFlexability)) + "  " + str(median(basicFlexability)) + "  " + str(median(Flexability))+"\n")
print("Originality: " + str(median(staticOriginality)) + "  " + str(median(basicOriginality)) + "  " + str(median(Originality))+"\n")

print("Min Scores Static     Basic      Inspiration:\n")
print("Fluency: " + str(min(staticFluency)) + "  " + str(min(basicFluency)) + "  " + str(min(Fluency))+"\n")
print("Flexability: " + str(min(staticFlexability)) + "  " + str(min(basicFlexability)) + "  " + str(min(Flexability))+"\n")
print("Originality: " + str(min(staticOriginality)) + "  " + str(min(basicOriginality)) + "  " + str(min(Originality))+"\n")

print("Max Scores Static     Basic      Inspiration:\n")
print("Fluency: " + str(max(staticFluency)) + "  " + str(max(basicFluency)) + "  " + str(max(Fluency))+"\n")
print("Flexability: " + str(max(staticFlexability)) + "  " + str(max(basicFlexability)) + "  " + str(max(Flexability))+"\n")
print("Originality: " + str(max(staticOriginality)) + "  " + str(max(basicOriginality)) + "  " + str(max(Originality))+"\n")


print("-------:\n")
print("Pairwise Comparison of Originality:\n")
print("Inspiration vs Basic:\n")
print("TukeyHsd: " + str(tukey_hsd(Originality,basicOriginality)) + "\n")
print("Inspiration vs Static:\n")
print("TukeyHsd: " + str(tukey_hsd(staticOriginality,Originality)) + "\n")
print("Basic vs Static:\n")
print("TukeyHsd: " + str(tukey_hsd(staticOriginality,basicOriginality)) + "\n")

print("-------:\n")
print("Pairwise Comparison of Flexibility:\n")
print("Inspiration vs Basic:\n")
print("TukeyHsd: " + str(tukey_hsd(basicFlexability,Flexability)) + "\n")
print("Inspiration vs Static:\n")
print("TukeyHsd: " + str(tukey_hsd(staticFlexability,Flexability)) + "\n")
print("Basic vs Static:\n")
print("TukeyHsd: " + str(tukey_hsd(staticFlexability,basicFlexability)) + "\n")

print("-------:\n")
print("Pairwise Comparison of Fluency:\n")
print("Inspiration vs Basic:\n")
print("TukeyHsd: " + str(tukey_hsd(basicFluency,Fluency)) + "\n")
print("Inspiration vs Static:\n")
print("TukeyHsd: " + str(tukey_hsd(staticFluency,Fluency)) + "\n")
print("Basic vs Static:\n")
print("TukeyHsd: " + str(tukey_hsd(staticFluency,basicFluency)) + "\n")


print(tukey_hsd(staticOriginality,basicOriginality))


print("Varianzhomogenität Originality Score: "+str(levene(staticOriginality, basicOriginality,Originality)))
print("Varianzhomogenität Flexability Score: "+str(levene(staticFlexability, basicFlexability,Flexability)))
print("Varianzhomogenität Fluency Score: "+str(levene(staticFluency, basicFluency,Fluency)))
print("OneWayAnova Originality Score: "+str(f_oneway(staticOriginality,basicOriginality,Originality)))
print("OneWayAnova Flexability Score: "+str(f_oneway(staticFlexability,basicFlexability,Flexability)))
print("OneWayAnova Fluency Score: "+str(f_oneway(staticFluency,basicFluency,Fluency)))



