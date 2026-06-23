import multiprocessing
from util.generateFile import generateFiles

def splitFiles(numFiles):
    fileCountPerLevel = [int(numFiles/4), int(numFiles/4), 
                        int(numFiles/4), int(numFiles/4)]
    fileCountPerLevel[0] += int(numFiles%4)
    
    return fileCountPerLevel