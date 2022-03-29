import json
from time import sleep

DATA_FILE = "program_data.json"


### Functions for managing contact lists ###
def addIpToRecents(ip):
    with open(DATA_FILE, "r+") as file:
        readFile = json.loads(file.read())
        if ip not in readFile["recents"]:
            readFile["recents"].append(ip)
            file.truncate(0)
            file.seek(0)
            file.write(json.dumps(readFile))


def addIpToContacts(alias, ip):
    with open(DATA_FILE, "r+") as file:
        readFile = json.loads(file.read())
        readFile["contacts"][alias] = ip
        file.truncate(0)
        file.seek(0)
        file.write(json.dumps(readFile))


def getRecents():
    with open(DATA_FILE, "r") as file:
        return json.loads(file.read())["recents"]


def getContacts():
    with open(DATA_FILE, "r") as file:
        return json.loads(file.read())["contacts"]


### Functions for managing contact lists ###

### Miscellaneous ###


def getIpAdress():
    from netifaces import interfaces, ifaddresses, AF_INET
    return ifaddresses(interfaces()[0])[AF_INET][0]['addr']


### Miscellaneous ###

### Threads ###


def samplethreadfunction():
    while True:
        print("Yaaay, me is a thread!")
        sleep(2)


### Threads ###

### Testing area ###

### Testing area ###