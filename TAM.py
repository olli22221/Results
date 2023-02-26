import json
import os


dir_path = os.getcwd()

pathToUserDataBasic = dir_path+"/rawData/fantasizefreelyBasic/userDataBasic"

pathToUserDataStatic = dir_path+"/rawData/fantasizefreelyStatic/userDataStatic"
pathToUserData = dir_path+"/rawData/fantasizefreely/userData"

paths = [pathToUserDataStatic, pathToUserDataBasic, pathToUserData]

for path in paths:
    PerceivedEaseOfUse = 0

    subjectCount = 0

    for dirs in os.listdir(path):
        pathToPostExperiment = path+ "/" + dirs + "/experiments/postExperiments.json"
        try:
            json_file = open(pathToPostExperiment)
            json_dict = json.load(json_file)
            PerceivedEaseOfUse+=json_dict["Learning to operate this creativity support tool would be easy for me."]+\
                json_dict["My interaction with this creativity support tool would be clear and understandable."]+ \
                json_dict["I would find this creativity support tool would be clear and understandable."] + \
                json_dict["It would be easy for me to become skillful at using this creativity support tool."] + \
                json_dict["I would find this creativity support tool easy to use."]

            subjectCount+=1
        except:
            print("Not a subject")
    PerceivedEaseOfUse/=subjectCount
    print("Results for " + path)
    print("Perceived Ease Of Use (PEU): "+ str(PerceivedEaseOfUse))