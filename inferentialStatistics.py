import json
import os

dir_path = os.getcwd()

pathToUserDataBasic = dir_path+"/rawData/fantasizefreelyBasic/userDataBasic"

pathToUserDataStatic = dir_path+"/rawData/fantasizefreelyStatic/userDataStatic"
pathToUserData = dir_path+"/rawData/fantasizefreely/userData"

paths = [pathToUserDataStatic, pathToUserDataBasic, pathToUserData]

ResultWorthEffortAvgFactorScoreStatic = []
ExplorationAvgFactorScoreStatic = []
CollaborationAvgFactorScoreStatic = []
ImmersionAvgFactorScoreStatic = []
ExpressivenessAvgFactorScoreStatic = []
EnjoymentAvgFactorScoreStatic = []
PerceivedEaseOfUseStatic =[]

ResultWorthEffortAvgFactorScoreBasic = []
ExplorationAvgFactorScoreBasic = []
CollaborationAvgFactorScoreBasic = []
ImmersionAvgFactorScoreBasic = []
ExpressivenessAvgFactorScoreBasic = []
EnjoymentAvgFactorScoreBasic = []
PerceivedEaseOfUseBasic = []

ResultWorthEffortAvgWeightedFactorScoreAI = []
ExplorationAvgWeightedFactorScoreAI = []
CollaborationAvgWeightedFactorScoreAI = []
ImmersionAvgWeightedFactorScoreAI = []
ExpressivenessAvgWeightedFactorScoreAI = []
EnjoymentAvgWeightedFactorScoreAI = []

ResultWorthEffortAvgFactorScoreAI = []
ExplorationAvgFactorScoreAI = []
CollaborationAvgFactorScoreAI = []
ImmersionAvgFactorScoreAI = []
ExpressivenessAvgFactorScoreAI = []
EnjoymentAvgFactorScoreAI = []
PerceivedEaseOfUseAI = []

for path in paths:


    ResultWorthEffortAvgFactorScore = []
    ExplorationAvgFactorScore = []
    CollaborationAvgFactorScore = []
    ImmersionAvgFactorScore = []
    ExpressivenessAvgFactorScore = []
    EnjoymentAvgFactorScore = []
    PerceivedEaseOfUse = []

    for dirs in os.listdir(path):
        pathToPostExperiment = path + "/" + dirs + "/experiments/postExperiments.json"
        try:
            json_file = open(pathToPostExperiment)
            json_dict = json.load(json_file)
            ResultWorthEffortAvgFactorCount = 0
            ExplorationAvgFactorCount = 0
            CollaborationAvgFactorCount = 0
            ImmersionAvgFactorCount = 0
            ExpressivenessAvgFactorCount = 0
            EnjoymentAvgFactorCount = 0
            pairedFactorArray = [json_dict["b1"], json_dict["b2"], json_dict["b3"], json_dict["b4"], json_dict["b5"],
                                 json_dict["b6"], json_dict["b7"], json_dict["b8"], json_dict["b9"], json_dict["b10"] \
                , json_dict["b11"], json_dict["b12"], json_dict["b13"], json_dict["b14"], json_dict["b15"]]
            for element in pairedFactorArray:
                if element == "Be creative and expressive":
                    ExpressivenessAvgFactorCount += 1
                elif element == "Work with other people":
                    CollaborationAvgFactorCount += 1
                elif element == "Produce results that are worth the effort I put in":
                    ResultWorthEffortAvgFactorCount += 1
                elif element == "Enjoy using the system or tool":
                    EnjoymentAvgFactorCount += 1
                elif element == "Become immersed in the activity":
                    ImmersionAvgFactorCount += 1
                elif element == "Explore many different ideas, outcomes, or possibilities":
                    ExplorationAvgFactorCount += 1

            PerceivedEaseOfUse.append(json_dict["Learning to operate this creativity support tool would be easy for me."]+\
                                      json_dict["My interaction with this creativity support tool would be clear and understandable."]+\
                                      json_dict["I would find this creativity support tool would be clear and understandable."]+\
                                      json_dict["It would be easy for me to become skillful at using this creativity support tool."]+\
                                      json_dict["I would find this creativity support tool easy to use."])

            EnjoymentAvgFactorScore.append(json_dict[
                                           "I would be happy to use the creativity support tool on a regular basis."] + \
                                       json_dict["I enjoyed using the creativity support tool."])
            ResultWorthEffortAvgFactorScore.append(json_dict[
                                                   "I was satisfied with what I got out of the creativity support tool."] + \
                                               json_dict[
                                                   "What I was able to produce was worth the effort I had to exert to produce it."])
            ExplorationAvgFactorScore.append(json_dict[
                                             "It was easy for me to explore many different ideas using the creativity support tool."] + \
                                         json_dict[
                                             "The creativity support tool was helpful in allowing me to track different ideas or possibilities."])
            CollaborationAvgFactorScore.append(json_dict[
                                               "The system or tool allowed other people to work with me easily."] + \
                                           json_dict[
                                               "It was really easy to share ideas and designs with other people inside this system or tool."])
            ExpressivenessAvgFactorScore.append(json_dict[
                                                "I was able to be very creative while doing the activity inside the creativity support tool."] + \
                                            json_dict["The creativity support tool allowed me to be very expressive."])
            ImmersionAvgFactorScore.append(json_dict[
                                           "My attention was fully tuned to the activity, and I forgot about the tool that I was using."] + \
                                       json_dict[
                                           "I became so absorbed in the activity that I forgot about the creativity support tool that I was using."])

            EnjoymentAvgWeightedFactorScoreAI.append(json_dict[
                                               "I would be happy to use the creativity support tool on a regular basis."] + \
                                           json_dict["I enjoyed using the creativity support tool."])
            ResultWorthEffortAvgWeightedFactorScore.append(json_dict[
                                                       "I was satisfied with what I got out of the creativity support tool."] + \
                                                   json_dict[
                                                       "What I was able to produce was worth the effort I had to exert to produce it."])
            ExplorationAvgWeightedFactorScore.append(json_dict[
                                                 "It was easy for me to explore many different ideas using the creativity support tool."] + \
                                             json_dict[
                                                 "The creativity support tool was helpful in allowing me to track different ideas or possibilities."])
            CollaborationAvgWeightedFactorScore.append(json_dict[
                                                   "The system or tool allowed other people to work with me easily."] + \
                                               json_dict[
                                                   "It was really easy to share ideas and designs with other people inside this system or tool."])
            ExpressivenessAvgWeightedFactorScore.append(json_dict[
                                                    "I was able to be very creative while doing the activity inside the creativity support tool."] + \
                                                json_dict[
                                                    "The creativity support tool allowed me to be very expressive."])
            ImmersionAvgWeightedFactorScore.append(json_dict[
                                               "My attention was fully tuned to the activity, and I forgot about the tool that I was using."] + \
                                           json_dict[
                                               "I became so absorbed in the activity that I forgot about the creativity support tool that I was using."])


        except:
            print("Not a subject")

    if "Static" in path:
        ResultWorthEffortAvgFactorScoreStatic = ResultWorthEffortAvgFactorScore
        ExplorationAvgFactorScoreStatic = ExplorationAvgFactorScore
        CollaborationAvgFactorScoreStatic = CollaborationAvgFactorScore
        ImmersionAvgFactorScoreStatic = ImmersionAvgFactorScore
        ExpressivenessAvgFactorScoreStatic = ExpressivenessAvgFactorScore
        EnjoymentAvgFactorScoreStatic = EnjoymentAvgFactorScore
        PerceivedEaseOfUseStatic = PerceivedEaseOfUse
    elif "Basic" in path:
        ResultWorthEffortAvgFactorScoreBasic = ResultWorthEffortAvgFactorScore
        ExplorationAvgFactorScoreBasic = ExplorationAvgFactorScore
        CollaborationAvgFactorScoreBasic = CollaborationAvgFactorScore
        ImmersionAvgFactorScoreBasic = ImmersionAvgFactorScore
        ExpressivenessAvgFactorScoreBasic = ExpressivenessAvgFactorScore
        EnjoymentAvgFactorScoreBasic = EnjoymentAvgFactorScore
        PerceivedEaseOfUseBasic = PerceivedEaseOfUse
    elif "fantasizefreely/userData" in path:
        ResultWorthEffortAvgFactorScoreAI = ResultWorthEffortAvgFactorScore
        ExplorationAvgFactorScoreAI = ExplorationAvgFactorScore
        CollaborationAvgFactorScoreAI = CollaborationAvgFactorScore
        ImmersionAvgFactorScoreAI = ImmersionAvgFactorScore
        ExpressivenessAvgFactorScoreAI = ExpressivenessAvgFactorScore
        EnjoymentAvgFactorScoreAI = EnjoymentAvgFactorScore
        PerceivedEaseOfUseAI = PerceivedEaseOfUse

from scipy.stats import f_oneway,kruskal,tukey_hsd,levene
from statistics import mean
#from scikit_posthocs import posthoc_dunn
from statistics import mean, stdev,median
print(f_oneway(ExpressivenessAvgFactorScoreStatic,ExpressivenessAvgFactorScoreBasic,ExpressivenessAvgFactorScoreAI))
print(f_oneway(ExplorationAvgFactorScoreStatic,ExplorationAvgFactorScoreBasic,ExplorationAvgFactorScoreAI))

print(kruskal(ExpressivenessAvgFactorScoreStatic,ExpressivenessAvgFactorScoreBasic,ExpressivenessAvgFactorScoreAI))
print(kruskal(ExplorationAvgFactorScoreStatic,ExplorationAvgFactorScoreBasic,ExplorationAvgFactorScoreAI))

print(tukey_hsd(ExpressivenessAvgFactorScoreStatic,ExpressivenessAvgFactorScoreAI))
print(tukey_hsd(ExplorationAvgFactorScoreStatic,ExplorationAvgFactorScoreAI))



print("Varianzhomogenität Expressiveness: "+str(levene(ExpressivenessAvgFactorScoreStatic, ExpressivenessAvgFactorScoreBasic,ExpressivenessAvgFactorScoreAI)))
print("Varianzhomogenität Enjoyment: "+str(levene(EnjoymentAvgFactorScoreStatic, EnjoymentAvgFactorScoreBasic,EnjoymentAvgFactorScoreAI)))
print("Varianzhomogenität Exploration: "+str(levene(ExplorationAvgFactorScoreStatic, ExplorationAvgFactorScoreBasic,ExplorationAvgFactorScoreAI)))
print("Varianzhomogenität ResultsWithEffort: "+str(levene(ResultWorthEffortAvgFactorScoreStatic, ResultWorthEffortAvgFactorScoreBasic,ResultWorthEffortAvgFactorScoreAI)))
print("Varianzhomogenität Immersion: "+str(levene(ImmersionAvgFactorScoreStatic, ImmersionAvgFactorScoreBasic,ImmersionAvgFactorScoreAI)))
print("Varianzhomogenität PEU: "+str(levene(PerceivedEaseOfUseStatic, PerceivedEaseOfUseBasic,PerceivedEaseOfUseAI)))


print("Perceived Enjoyment:")
print(f_oneway(EnjoymentAvgFactorScoreStatic,EnjoymentAvgFactorScoreBasic,EnjoymentAvgFactorScoreAI))
print(kruskal(EnjoymentAvgFactorScoreStatic,EnjoymentAvgFactorScoreBasic,EnjoymentAvgFactorScoreAI))
print("mean of Static"+str(mean(EnjoymentAvgFactorScoreStatic)))
print(mean(EnjoymentAvgFactorScoreBasic))
print(mean(EnjoymentAvgFactorScoreAI))
print(stdev(EnjoymentAvgFactorScoreStatic))
print(stdev(EnjoymentAvgFactorScoreBasic))
print(stdev(EnjoymentAvgFactorScoreAI))
print(median(EnjoymentAvgFactorScoreStatic))
print(median(EnjoymentAvgFactorScoreBasic))
print(median(EnjoymentAvgFactorScoreAI))
print(min(EnjoymentAvgFactorScoreStatic))
print(min(EnjoymentAvgFactorScoreBasic))
print(min(EnjoymentAvgFactorScoreAI))
print(max(EnjoymentAvgFactorScoreStatic))
print(max(EnjoymentAvgFactorScoreBasic))
print(max(EnjoymentAvgFactorScoreAI))


print("---------------------")

print(tukey_hsd(EnjoymentAvgFactorScoreStatic,EnjoymentAvgFactorScoreBasic))
print(tukey_hsd(EnjoymentAvgFactorScoreStatic,EnjoymentAvgFactorScoreAI))
print(tukey_hsd(EnjoymentAvgFactorScoreBasic,EnjoymentAvgFactorScoreAI))

print("Perceived Ease Of Use:")
print(f_oneway(PerceivedEaseOfUseStatic,PerceivedEaseOfUseBasic,PerceivedEaseOfUseAI))
print(kruskal(PerceivedEaseOfUseStatic,PerceivedEaseOfUseBasic,PerceivedEaseOfUseAI))
print(mean(PerceivedEaseOfUseStatic))
print(mean(PerceivedEaseOfUseBasic))
print(mean(PerceivedEaseOfUseAI))


print(tukey_hsd(PerceivedEaseOfUseStatic,EnjoymentAvgFactorScoreBasic))
print(tukey_hsd(PerceivedEaseOfUseStatic,PerceivedEaseOfUseAI))
print(tukey_hsd(PerceivedEaseOfUseAI,PerceivedEaseOfUseBasic))
print("Perceived Collaboration: ")
print(mean(CollaborationAvgFactorScoreStatic))
print(mean(CollaborationAvgFactorScoreBasic))
print(mean(CollaborationAvgFactorScoreAI))
print(stdev(CollaborationAvgFactorScoreStatic))
print(stdev(CollaborationAvgFactorScoreBasic))
print(stdev(CollaborationAvgFactorScoreAI))
print("Perceived Exploration:")
print(f_oneway(ExplorationAvgFactorScoreStatic,ExplorationAvgFactorScoreBasic,ExplorationAvgFactorScoreAI))
print(kruskal(ExplorationAvgFactorScoreStatic,ExplorationAvgFactorScoreBasic,ExplorationAvgFactorScoreAI))

print(mean(ExplorationAvgFactorScoreStatic))
print(mean(ExplorationAvgFactorScoreBasic))
print(mean(ExplorationAvgFactorScoreAI))
print(stdev(ExplorationAvgFactorScoreStatic))
print(stdev(ExplorationAvgFactorScoreBasic))
print(stdev(ExplorationAvgFactorScoreAI))
print(median(ExplorationAvgFactorScoreStatic))
print(median(ExplorationAvgFactorScoreBasic))
print(median(ExplorationAvgFactorScoreAI))
print(min(ExplorationAvgFactorScoreStatic))
print(min(ExplorationAvgFactorScoreBasic))
print(min(ExplorationAvgFactorScoreAI))
print(max(ExplorationAvgFactorScoreStatic))
print(max(ExplorationAvgFactorScoreBasic))
print(max(ExplorationAvgFactorScoreAI))


#print(posthoc_dunn([ExplorationAvgFactorScoreStatic,ExplorationAvgFactorScoreBasic]))
#print(posthoc_dunn([ExplorationAvgFactorScoreStatic,ExplorationAvgFactorScoreAI]))
#print(posthoc_dunn([ExplorationAvgFactorScoreAI,ExplorationAvgFactorScoreBasic]))
print("Perceived Expressiveness:")
print(f_oneway(ExpressivenessAvgFactorScoreStatic,ExpressivenessAvgFactorScoreBasic,ExpressivenessAvgFactorScoreAI))
print(kruskal(ExpressivenessAvgFactorScoreStatic,ExpressivenessAvgFactorScoreBasic,ExpressivenessAvgFactorScoreAI))

print(mean(ExpressivenessAvgFactorScoreStatic))
print(mean(ExpressivenessAvgFactorScoreBasic))
print(mean(ExpressivenessAvgFactorScoreAI))
print(stdev(ExpressivenessAvgFactorScoreStatic))
print(stdev(ExpressivenessAvgFactorScoreBasic))
print(stdev(ExpressivenessAvgFactorScoreAI))
print(median(ExpressivenessAvgFactorScoreStatic))
print(median(ExpressivenessAvgFactorScoreBasic))
print(median(ExpressivenessAvgFactorScoreAI))
print(min(ExpressivenessAvgFactorScoreStatic))
print(min(ExpressivenessAvgFactorScoreBasic))
print(min(ExpressivenessAvgFactorScoreAI))
print(max(ExpressivenessAvgFactorScoreStatic))
print(max(ExpressivenessAvgFactorScoreBasic))
print(max(ExpressivenessAvgFactorScoreAI))
#print(posthoc_dunn([ExpressivenessAvgFactorScoreStatic,ExpressivenessAvgFactorScoreBasic]))
#print(posthoc_dunn([ExpressivenessAvgFactorScoreStatic,ExpressivenessAvgFactorScoreAI]))
#print(posthoc_dunn([ExpressivenessAvgFactorScoreBasic,ExpressivenessAvgFactorScoreAI]))
print("Perceived Immersion:")
print(f_oneway(ImmersionAvgFactorScoreStatic,ImmersionAvgFactorScoreBasic,ImmersionAvgFactorScoreAI))
print(mean(ImmersionAvgFactorScoreStatic))
print(mean(ImmersionAvgFactorScoreBasic))
print(mean(ImmersionAvgFactorScoreAI))
print(stdev(ImmersionAvgFactorScoreStatic))
print(stdev(ImmersionAvgFactorScoreBasic))
print(stdev(ImmersionAvgFactorScoreAI))

print("Perceived ResultsWithEffort:")
print(f_oneway(ResultWorthEffortAvgFactorScoreStatic,ResultWorthEffortAvgFactorScoreBasic,ResultWorthEffortAvgFactorScoreAI))
print(mean(ResultWorthEffortAvgFactorScoreStatic))
print(mean(ResultWorthEffortAvgFactorScoreBasic))
print(mean(ResultWorthEffortAvgFactorScoreAI))
print(stdev(ResultWorthEffortAvgFactorScoreStatic))
print(stdev(ResultWorthEffortAvgFactorScoreBasic))
print(stdev(ResultWorthEffortAvgFactorScoreAI))

