import json

with open("lisas.json") as JsonFile:
    data= json.load(JsonFile)
    jsonData= data["tracks"]["items"]

    for trackId in jsonData:
        values = trackId["id"]

        
        print(values)