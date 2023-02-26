import json
import os

import csv


dir_path = os.getcwd()

pathToUserDataBasic = dir_path+"/rawData/fantasizefreelyBasic/userDataBasic"

pathToUserDataStatic = dir_path+"/rawData/studyData/fantasizefreelyStatic/userDataStatic"
pathToUserData = dir_path+"/rawData/ExperimentData/fantasizefreely/userData"

with open('StaticPostExperimentFreeText.csv', 'w', encoding='utf-8') as inspiration:
    writer = csv.writer(inspiration, delimiter=',')
    for dirs in os.listdir(pathToUserDataStatic):
        try:
            pathToPostExperiment = pathToUserDataStatic + "/" + dirs + "/experiments/postExperiments.json"

            json_file = open(pathToPostExperiment)
            json_dict = json.load(json_file)

            freetext_1 = json_dict["What did you most like about the tool?"]
            freetext_2 = json_dict["What did you dislike about the tool?"]
            freetext_3 = json_dict["If given a chance, what would you change or add in the tool?"]




            row = []
            row.append(dirs)
            row.append(freetext_1)
            row.append(freetext_2)
            row.append(freetext_3)



            writer.writerow(row)
        except:
            print("Not a subject")
"""
with open('BasicPostExperimentFreeText.csv', 'w', encoding='utf-8') as inspiration:
    writer = csv.writer(inspiration, delimiter=',')
    for dirs in os.listdir(pathToUserDataBasic):
        try:
            pathToPostExperiment = pathToUserDataBasic + "/" + dirs + "/experiments/postExperiments.json"

            json_file = open(pathToPostExperiment)
            json_dict = json.load(json_file)
            freetext_1 = json_dict["What do you think of the scores you received?"]
            freetext_2 = json_dict["Do you think you progressed with your scores?"]
            freetext_3 = json_dict["How did you like the Musicat's graphical prediction?"]
            freetext_4 = json_dict["Did you find the scores to be useful?"]
            freetext_5 = json_dict["What did you most like about the tool?"]
            freetext_6 = json_dict["What did you dislike about the tool?"]
            freetext_7 = json_dict["If given a chance, what would you change or add in the tool?"]




            row = []
            row.append(dirs)
            row.append(freetext_1)
            row.append(freetext_2)
            row.append(freetext_3)
            row.append(freetext_4)
            row.append(freetext_5)
            row.append(freetext_6)
            row.append(freetext_7)


            writer.writerow(row)
        except:
            print("Not a subject") """

"""with open('InspirationPostExperimentFreeText.csv', 'w', encoding='utf-8') as inspiration:
    writer = csv.writer(inspiration, delimiter=',')
    for dirs in os.listdir(pathToUserData):
        try:
            pathToPostExperiment = pathToUserData + "/" + dirs + "/experiments/postExperiments.json"

            json_file = open(pathToPostExperiment)
            json_dict = json.load(json_file)
            freetext_1 = json_dict["How many times did you click the \u201cInspiration\u201d button?"]
            freetext_2 = json_dict["Do you feel the inspirations sparked new ideas for your composition?"]
            freetext_3 = json_dict["How relevant were the inspirations to your music?"]
            freetext_4 = json_dict["Did you update your composition based on the suggestions? If yes, what were the updates you made to your music?"]
            freetext_5 = json_dict["What do you think of the scores you received?"]
            freetext_6 = json_dict["Do you think you progressed with your scores?"]
            freetext_7 = json_dict["How did you like the Musicat's graphical prediction?"]
            freetext_8 = json_dict["Did you find the scores to be useful?"]
            freetext_9 = json_dict["What did you most like about the tool?"]
            freetext_10 = json_dict["What did you dislike about the tool?"]
            freetext_11 = json_dict["If given a chance, what would you change or add in the tool?"]



            row = []
            row.append(dirs)
            row.append(freetext_1)
            row.append(freetext_2)
            row.append(freetext_3)
            row.append(freetext_4)
            row.append(freetext_5)
            row.append(freetext_6)
            row.append(freetext_7)
            row.append(freetext_8)
            row.append(freetext_9)
            row.append(freetext_10)
            row.append(freetext_11)

            writer.writerow(row)
        except:
            print("Not a subject")"""

