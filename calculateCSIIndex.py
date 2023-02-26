import json
import os
from statistics import mean, stdev,median
dir_path = os.getcwd()


pathToUserDataBasic = dir_path+"/rawData/fantasizefreelyBasic/userDataBasic"

pathToUserDataStatic = dir_path+"/rawData/fantasizefreelyStatic/userDataStatic"
pathToUserData = dir_path+"/rawData/fantasizefreely/userData"

paths = [pathToUserDataStatic, pathToUserDataBasic, pathToUserData]

for path in paths:



    ResultWorthEffortAvgFactorScore = 0
    ExplorationAvgFactorScore = 0
    CollaborationAvgFactorScore = 0
    ImmersionAvgFactorScore = 0
    ExpressivenessAvgFactorScore = 0
    EnjoymentAvgFactorScore = 0

    ResultWorthEffortAvgFactorCount = 0
    ExplorationAvgFactorCount = 0
    CollaborationAvgFactorCount = 0
    ImmersionAvgFactorCount = 0
    ExpressivenessAvgFactorCount = 0
    EnjoymentAvgFactorCount = 0

    ResultWorthEffortFactorCount = []
    ExplorationFactorCount = []
    CollaborationFactorCount = []
    ImmersionFactorCount = []
    ExpressivenessFactorCount = []
    EnjoymentFactorCount = []

    subjectCount = 0

    for dirs in os.listdir(path):

        pathToPostExperiment = path+ "/" + dirs + "/experiments/postExperiments.json"
        try:
            json_file = open(pathToPostExperiment)
            json_dict = json.load(json_file)
            ResultWorthEffortAvgFactorCount = 0
            ExplorationAvgFactorCount = 0
            CollaborationAvgFactorCount = 0
            ImmersionAvgFactorCount = 0
            ExpressivenessAvgFactorCount = 0
            EnjoymentAvgFactorCount = 0

            EnjoymentAvgFactorScore += json_dict["I would be happy to use the creativity support tool on a regular basis."]+json_dict["I enjoyed using the creativity support tool."]
            ResultWorthEffortAvgFactorScore += json_dict[
                                           "I was satisfied with what I got out of the creativity support tool."] + \
                                       json_dict["What I was able to produce was worth the effort I had to exert to produce it."]
            ExplorationAvgFactorScore += json_dict[
                                           "It was easy for me to explore many different ideas using the creativity support tool."] + \
                                       json_dict["The creativity support tool was helpful in allowing me to track different ideas or possibilities."]
            CollaborationAvgFactorScore += json_dict[
                                           "The system or tool allowed other people to work with me easily."] + \
                                       json_dict["It was really easy to share ideas and designs with other people inside this system or tool."]
            ExpressivenessAvgFactorScore += json_dict[
                                           "I was able to be very creative while doing the activity inside the creativity support tool."] + \
                                       json_dict["The creativity support tool allowed me to be very expressive."]
            ImmersionAvgFactorScore += json_dict[
                                           "My attention was fully tuned to the activity, and I forgot about the tool that I was using."] + \
                                       json_dict["I became so absorbed in the activity that I forgot about the creativity support tool that I was using."]
            pairedFactorArray = [json_dict["b1"],json_dict["b2"],json_dict["b3"],json_dict["b4"],json_dict["b5"],json_dict["b6"],json_dict["b7"],json_dict["b8"],json_dict["b9"],json_dict["b10"] \
                ,json_dict["b11"],json_dict["b12"],json_dict["b13"],json_dict["b14"],json_dict["b15"]]
            for element in pairedFactorArray:
                if element == "Be creative and expressive":
                    ExpressivenessAvgFactorCount+=1
                elif element == "Work with other people":
                    CollaborationAvgFactorCount+=1
                elif element == "Produce results that are worth the effort I put in":
                    ResultWorthEffortAvgFactorCount+=1
                elif element == "Enjoy using the system or tool":
                    EnjoymentAvgFactorCount+=1
                elif element == "Become immersed in the activity":
                    ImmersionAvgFactorCount+=1
                elif element == "Explore many different ideas, outcomes, or possibilities":
                    ExplorationAvgFactorCount+=1
            subjectCount = subjectCount + 1
            ResultWorthEffortFactorCount.append(ResultWorthEffortAvgFactorCount)
            CollaborationFactorCount.append(CollaborationAvgFactorCount)
            ExpressivenessFactorCount.append(ExpressivenessAvgFactorCount)
            ExplorationFactorCount.append(ExplorationAvgFactorCount)
            ImmersionFactorCount.append(ImmersionAvgFactorCount)
            EnjoymentFactorCount.append(EnjoymentAvgFactorCount)



        except:
            print("Not a subject")
    if "Static" in path:
        print("STATIC")
        print("Mean of Enjoyment: "+str(mean(EnjoymentFactorCount)))
        print("Stdev of Enjoyment: " + str(stdev(EnjoymentFactorCount)))
        print("Mean of Expressiveness: " + str(mean(ExpressivenessFactorCount)))
        print("Stdev of Expressiveness: " + str(stdev(ExpressivenessFactorCount)))
        print("Mean of Exploration: " + str(mean(ExplorationFactorCount)))
        print("Stdev of Exploration: " + str(stdev(ExplorationFactorCount)))
        print("Mean of Collaboration: " + str(mean(CollaborationFactorCount)))
        print("Stdev of Collaboration: " + str(stdev(CollaborationFactorCount)))
        print("Mean of Immersion: " + str(mean(ImmersionFactorCount)))
        print("Stdev of Immersion: " + str(stdev(ImmersionFactorCount)))
        print("Mean of ResultsWorthEffort: " + str(mean(ResultWorthEffortFactorCount)))
        print("Stdev of ResultsWorthEffort: " + str(stdev(ResultWorthEffortFactorCount)))

    if "Basic" in path:
        print("BASIC")
        print("Mean of Enjoyment: "+str(mean(EnjoymentFactorCount)))
        print("Stdev of Enjoyment: " + str(stdev(EnjoymentFactorCount)))
        print("Mean of Expressiveness: " + str(mean(ExpressivenessFactorCount)))
        print("Stdev of Expressiveness: " + str(stdev(ExpressivenessFactorCount)))
        print("Mean of Exploration: " + str(mean(ExplorationFactorCount)))
        print("Stdev of Exploration: " + str(stdev(ExplorationFactorCount)))
        print("Mean of Collaboration: " + str(mean(CollaborationFactorCount)))
        print("Stdev of Collaboration: " + str(stdev(CollaborationFactorCount)))
        print("Mean of Immersion: " + str(mean(ImmersionFactorCount)))
        print("Stdev of Immersion: " + str(stdev(ImmersionFactorCount)))
        print("Mean of ResultsWorthEffort: " + str(mean(ResultWorthEffortFactorCount)))
        print("Stdev of ResultsWorthEffort: " + str(stdev(ResultWorthEffortFactorCount)))
    if "fantasizefreely/userData" in path:
        print("Inspiration")
        print("Mean of Enjoyment: "+str(mean(EnjoymentFactorCount)))
        print("Stdev of Enjoyment: " + str(stdev(EnjoymentFactorCount)))
        print("Mean of Expressiveness: " + str(mean(ExpressivenessFactorCount)))
        print("Stdev of Expressiveness: " + str(stdev(ExpressivenessFactorCount)))
        print("Mean of Exploration: " + str(mean(ExplorationFactorCount)))
        print("Stdev of Exploration: " + str(stdev(ExplorationFactorCount)))
        print("Mean of Collaboration: " + str(mean(CollaborationFactorCount)))
        print("Stdev of Collaboration: " + str(stdev(CollaborationFactorCount)))
        print("Mean of Immersion: " + str(mean(ImmersionFactorCount)))
        print("Stdev of Immersion: " + str(stdev(ImmersionFactorCount)))
        print("Mean of ResultsWorthEffort: " + str(mean(ResultWorthEffortFactorCount)))
        print("Stdev of ResultsWorthEffort: " + str(stdev(ResultWorthEffortFactorCount)))


    ExpressivenessAvgFactorCount/=subjectCount
    ExpressivenessAvgFactorScore/=subjectCount
    EnjoymentAvgFactorCount/=subjectCount
    EnjoymentAvgFactorScore/=subjectCount
    CollaborationAvgFactorCount/=subjectCount
    CollaborationAvgFactorScore/=subjectCount
    ImmersionAvgFactorCount/=subjectCount
    ImmersionAvgFactorScore/=subjectCount
    ResultWorthEffortAvgFactorCount/=subjectCount
    ResultWorthEffortAvgFactorScore/=subjectCount
    ExplorationAvgFactorCount/=subjectCount
    ExplorationAvgFactorScore/=subjectCount

    print("Results for "+path)
    print("Results Worth Effort    Avg Factor Counts: " + str(ResultWorthEffortAvgFactorCount) + "  Avg Factor Score: "+ str(ResultWorthEffortAvgFactorScore) +" Avg Weighted Factor Score: "+str(ResultWorthEffortAvgFactorCount*ResultWorthEffortAvgFactorScore) )
    print("Exploration    Avg Factor Counts: " + str(
        ExplorationAvgFactorCount) + "  Avg Factor Score: " + str(ExplorationAvgFactorScore)  +" Avg Weighted Factor Score: "+str(ExpressivenessAvgFactorCount*ExplorationAvgFactorScore) )
    print("Collaboration    Avg Factor Counts: " + str(
        CollaborationAvgFactorCount) + "  Avg Factor Score: " + str(CollaborationAvgFactorScore)  +" Avg Weighted Factor Score: "+str(CollaborationAvgFactorCount*CollaborationAvgFactorScore) )
    print("Immersion    Avg Factor Counts: " + str(
        ImmersionAvgFactorCount) + "  Avg Factor Score: " + str(ImmersionAvgFactorScore)  +" Avg Weighted Factor Score: "+str(ImmersionAvgFactorCount*ImmersionAvgFactorScore) )
    print("Expressiveness    Avg Factor Counts: " + str(
        ExpressivenessAvgFactorCount) + "  Avg Factor Score: " + str(ExpressivenessAvgFactorScore)  +" Avg Weighted Factor Score: "+str(ExpressivenessAvgFactorCount*ExpressivenessAvgFactorScore) )
    print("Enjoyment    Avg Factor Counts: " + str(
        EnjoymentAvgFactorCount) + "  Avg Factor Score: " + str(EnjoymentAvgFactorScore)  +" Avg Weighted Factor Score: "+str(EnjoymentAvgFactorCount*EnjoymentAvgFactorScore) )
    print("CSI: "+ str(((ResultWorthEffortAvgFactorCount*ResultWorthEffortAvgFactorScore)+(ExpressivenessAvgFactorCount*ExplorationAvgFactorScore)+(CollaborationAvgFactorCount*CollaborationAvgFactorScore)+(ImmersionAvgFactorCount*ImmersionAvgFactorScore)+(ExpressivenessAvgFactorCount*ExpressivenessAvgFactorScore)+(EnjoymentAvgFactorCount*EnjoymentAvgFactorScore))/3))






