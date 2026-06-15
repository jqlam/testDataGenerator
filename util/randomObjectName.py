import random
import string
from datetime import datetime

def randomReference():
    char = random.randint(0, 61)
    if char < 10:
        return str(char)
    else:
        return random.choice(string.ascii_letters)
        
def randomObjectName(oneOff=True):
    if oneOff: #Is used for not list
        random.seed(int(datetime.now().timestamp()))
    randomName = ""
    nameLength = random.randint(10, 50)
    for i in range(nameLength):
        randomName += randomReference()
    return randomName

def listRandomObjectNames(numNames: int, offset = 0):
    random.seed(int(datetime.now().timestamp()) + offset)
    names = []
    for i in range(numNames):
        names.append(randomObjectName(False))
    return names