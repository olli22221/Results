import json
import os

import csv


dir_path = os.getcwd()

pathToUserDataBasic = dir_path+"/rawData/fantasizefreelyBasic/userDataBasic"

pathToUserDataStatic = dir_path+"/rawData/fantasizefreelyStatic/userDataStatic"
pathToUserData = dir_path+"/rawData/fantasizefreely/userData"

with open('StaticPostExperimentQuestions.csv', 'w', encoding='utf-8') as inspiration:
    writer = csv.writer(inspiration, delimiter=',')
    for dirs in os.listdir(pathToUserDataStatic):
        try:
            pathToPostExperiment = pathToUserDataStatic + "/" + dirs + "/experiments/postExperiments.json"

            json_file = open(pathToPostExperiment)
            json_dict = json.load(json_file)
            Enjoyment_1 = json_dict["I would be happy to use the creativity support tool on a regular basis."]
            Enjoyment_2 =json_dict["I enjoyed using the creativity support tool."]
            ResultWorthEffort1 = json_dict["I was satisfied with what I got out of the creativity support tool."]
            ResultWorthEffort2 = json_dict["What I was able to produce was worth the effort I had to exert to produce it."]
            Exploration1 = json_dict["It was easy for me to explore many different ideas using the creativity support tool."]
            Exploration2 = json_dict["The creativity support tool was helpful in allowing me to track different ideas or possibilities."]
            Collaboration1 = json_dict["The system or tool allowed other people to work with me easily."]
            Collaboration2 = json_dict["It was really easy to share ideas and designs with other people inside this system or tool."]
            Expressiveness1 = json_dict["I was able to be very creative while doing the activity inside the creativity support tool."]
            Expressiveness2 = json_dict["The creativity support tool allowed me to be very expressive."]
            Immersion1 = json_dict["My attention was fully tuned to the activity, and I forgot about the tool that I was using."]
            Immersion2 = json_dict["I became so absorbed in the activity that I forgot about the creativity support tool that I was using."]
            PerceivedEaseOfUse1 = json_dict["Learning to operate this creativity support tool would be easy for me."]
            PerceivedEaseOfUse2 = json_dict["My interaction with this creativity support tool would be clear and understandable."]
            PerceivedEaseOfUse3 = json_dict["I would find this creativity support tool would be clear and understandable."]
            PerceivedEaseOfUse4 = json_dict["It would be easy for me to become skillful at using this creativity support tool."]
            PerceivedEaseOfUse5 = json_dict["I would find this creativity support tool easy to use."]

            row = []
            row.append(dirs)
            row.append(Enjoyment_1)
            row.append(Enjoyment_2)
            row.append(ResultWorthEffort1)
            row.append(ResultWorthEffort2)
            row.append(Exploration1)
            row.append(Exploration2)
            row.append(Collaboration1)
            row.append(Collaboration2)
            row.append(Expressiveness1)
            row.append(Expressiveness2)
            row.append(Immersion1)
            row.append(Immersion2)
            row.append(PerceivedEaseOfUse1)
            row.append(PerceivedEaseOfUse2)
            row.append(PerceivedEaseOfUse3)
            row.append(PerceivedEaseOfUse4)
            row.append(PerceivedEaseOfUse5)
            writer.writerow(row)
        except:
            print("Not a subject")

