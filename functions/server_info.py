import json

def createServerFile(filename):
        with open(filename, "w") as file:
                template = {}

                temp = json.dumps(template, indent = 4)
                file.write(temp)

def loadServersInfo(filename):
        with open(filename, "r") as file:
                return json.load(file)

def addServer(filename, serverID, channelID):
        temp = {
                f"{serverID}": {
                        "selected_channel": f"{channelID}"
                }
        }

        with open(filename, "r") as file:
                data = json.load(file)

        data.update(temp)

        with open(filename, "w") as file:
                json.dump(data, file, indent = 4)

def changeChannel(filename, serverID, channelID):
        temp = {
                f"{serverID}": {
                        "selected_channel": f"{channelID}"
                }
        }

        with open(filename, "r") as file:
                data = json.load(file)

        data.pop(f"{serverID}", None)
        data.update(temp)
        
        with open(filename, "w") as file:
                json.dump(data, file, indent = 4)

def deleteServer(filename, serverID):
        with open(filename, "r") as file:
                data = json.load(file)

        data.pop(f"{serverID}", None)

        with open(filename, "w") as file:
                json.dump(data, file, indent = 4)

