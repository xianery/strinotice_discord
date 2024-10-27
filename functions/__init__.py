import json

def createConfig():
        with open("token.json", "w") as file:
                cfg = {
                        "token": "<insert token here>", 
                        "prefix": "/"
                }

                temp = json.dumps(cfg, indent=4)
                file.write(temp)