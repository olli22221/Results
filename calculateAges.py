import json
import os

dir_path = os.getcwd()

pathToUserDataBasic = dir_path+"/rawData/fantasizefreelyBasic/userDataBasic"

pathToUserDataStatic = dir_path+"/rawData/fantasizefreelyStatic/userDataStatic"
pathToUserData = dir_path+"/rawData/fantasizefreely/userData"

paths = [pathToUserDataStatic, pathToUserDataBasic, pathToUserData]
subjectCount = 0

participants_18_24 = 0
participants_25_34 = 0
participants_35_44 = 0
participants_45_above = 0

for path in paths:
    for dirs in os.listdir(path):
        pathToPostExperiment = path + "/" + dirs + "/experiments/postExperiments.json"
        pathToPreExperiment = path+ "/" + dirs + "/experiments/preExperiments.json"
        try:
            json_file = open(pathToPostExperiment)
            json_file = open(pathToPreExperiment)
            json_dict = json.load(json_file)
            json_dict = json.loads(json_dict)
            age = int(json_dict["age"])

            if age < 25:
                participants_18_24+=1
            elif age > 24 and age < 35:
                participants_25_34+=1
            elif age > 34 and age < 45:
                participants_35_44+=1
            elif age > 44:
                participants_45_above+=1
            subjectCount+=1
        except Exception as e:
            print(e)

print(str(participants_18_24)+" participants"+ "(" +str((participants_18_24/subjectCount)*100) + ") are aged between 18 and 24")
print(str(participants_25_34)+" participants"+ "(" +str((participants_25_34/subjectCount)*100) + ") are aged between 25 and 34")
print(str(participants_35_44)+" participants"+ "(" +str((participants_35_44/subjectCount)*100) + ") are aged between 35 and 44")
print(str(participants_45_above)+" participants"+ "(" +str((participants_45_above/subjectCount)*100) + ") are aged above 45")

print(subjectCount)