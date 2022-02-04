import json

with open("lisas.json") as JsonFile:
    data= json.load(JsonFile)
    jsonData= data["tracks"]["items"]
    tracksArr =[]

    for trackId in jsonData:
        values = trackId["id"]
        tracksArr.append(values)

        
        print(values)
    print(tracksArr)