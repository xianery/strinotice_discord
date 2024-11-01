import json

def createConfig(filename):
        data = {
                "token": "<insert token here>", 
                "prefix": "/",
                "latest_post_date": ""
        }
        
        with open(filename, "w") as file:
                json.dump(data, file, indent = 4)

def updatePostDate(filename, date):
        temp = {
                "latest_post_date": date
        }

        with open(filename, "r") as file:
                data = json.load(file)

        data.pop("latest_post_date", None)
        data.update(temp)

        with open(filename, "w") as file:
                json.dump(data, file, indent = 4)

def readConfig(filename):
        with open(filename, "r") as file:
                return json.load(file)