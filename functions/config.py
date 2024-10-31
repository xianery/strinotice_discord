import json

def createConfig(filename):
        with open(filename, "w") as file:
                cfg = {
                        "token": "<insert token here>", 
                        "prefix": "/"
                }

                temp = json.dumps(cfg, indent = 4)
                file.write(temp)

def readConfig(filename):
        with open(filename, "r") as file:
                return json.load(file)