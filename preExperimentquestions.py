import json
import os

import csv


dir_path = os.getcwd()

pathToUserDataBasic = dir_path+"/../ExperimentData/fantasizefreelyBasic/userDataBasic"

pathToUserDataStatic = dir_path+"/../studyData/fantasizefreelyStatic/userDataStatic"
pathToUserData = dir_path+"/../ExperimentData/fantasizefreely/userData"

with open('StaticPreExperimentsQuestions.csv', 'w', encoding='utf-8') as inspiration:
    writer = csv.writer(inspiration, delimiter=',')
    for dirs in os.listdir(pathToUserDataStatic):
        pathToPostExperiment = pathToUserDataStatic + "/" + dirs + "/experiments/postExperiments.json"
        pathToPreExperiment = pathToUserDataStatic + "/" + dirs + "/experiments/preExperiments.json"
        try:


            json_file_ = open(pathToPostExperiment)
            json_file = open(pathToPreExperiment)
            json_dict = json.load(json_file)
            json_dict = json.loads(json_dict)
            print(type(json_dict))


            initials = json_dict["initials"]
            age = json_dict["age"]
            gender = json_dict["gender"]
            country = json_dict["country"]
            areaOfFocus = json_dict["Area of focus"]
            musicExperience = json_dict["How is your experience with music"]




            row = []
            row.append(dirs)
            row.append(initials)
            row.append(age)
            row.append(gender)
            row.append(country)
            row.append(areaOfFocus)
            row.append(musicExperience)


            writer.writerow(row)
        except:
            print("Not a subject")
