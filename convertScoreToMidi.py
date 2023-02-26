from music21 import *

import json
import os
dir_path = os.getcwd()
compToMidi = {"g/3":55,"a/3":57,"b/3":59,"c/4":60,"d/4":62,"e/4":64,"f/4":65,"g/4":67,"a/4":69,"b/4":71,"c/5":72
              ,"d/5":74,"e/5":76,"f/5":77,"g/5":79,"a/5":81,"b/5":83,"c/6":84}


durationDict={"16":0.25,"8d":0.5, "q":1.0,"h":2.0, "w":4.0}

pathToUserDataBasic = dir_path+"/rawData/fantasizefreelyBasic/userDataBasic"

pathToUserDataStatic = dir_path+"/rawData/fantasizefreelyStatic/userDataStatic"
pathToUserData = dir_path+"/rawData/fantasizefreely/userData"


paths = [pathToUserDataStatic, pathToUserDataBasic, pathToUserData]

for path in paths:
    for dirs in os.listdir(path):
        if "0c554d1c" in dirs:
            continue
        pathToCompositions = path + "/" + dirs + "/compositions"
        for composition  in os.listdir(pathToCompositions):
            pathToComposition = pathToCompositions+"/"+composition
            print(pathToComposition)
            json_file = open(pathToComposition+"/compositionData.json")
            json_dict = json.load(json_file)
            json_dict = json.loads(json_dict)


            stream1 = stream.Stream()
            for elem in json_dict:
                for el in elem:

                    noteType = el['type']
                    noteDuration = el['duration']
                    shifted = el['accented']

                    if shifted == 1:
                        chr = noteType[0][0].upper()
                        resNote = chr + "#" + noteType[0][2]
                        n = note.Note(resNote)

                        n.duration.quarterLength = durationDict[noteDuration]
                        stream1.append(n)
                    else:

                        chr = noteType[0][0].upper()
                        resNote = chr + noteType[0][2]
                        n = note.Note(resNote)
                        n.duration.quarterLength = durationDict[noteDuration]
                        stream1.append(n)
            mf = midi.translate.streamToMidiFile(stream1)
            mf.open(pathToComposition+'/composition.mid', 'wb')
            mf.write()
            mf.close()
            parsed = converter.parse(pathToComposition+'/composition.mid')
            #parsed.write(pathToComposition+'composition.png')

            parsed.show()








