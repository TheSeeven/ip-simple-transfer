import json


def addIpToRecents(ip):
    with open("ipLists.json", "r") as file:
        readFile = json.loads(file.read())
        if ip not in readFile["recents"]:
            readFile["recents"].append(ip)
            with open(file.name, "w+") as result:
                result.write(json.dumps(readFile))


def addIpToContacts(alias, ip):
    with open("ipLists.json", "r") as file:
        readFile = json.loads(file.read())
        readFile["contacts"][alias] = ip
        with open(file.name, "w+") as result:
            result.write(json.dumps(readFile))


def getRecents():
    with open("ipLists.json", "r") as file:
        return json.loads(file.read())["recents"]


def getContacts():
    with open("ipLists.json", "r") as file:
        return json.loads(file.read())["contacts"]
