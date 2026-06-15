from util.generateTXT import generateTXT
from util.generateDOCX import generateDOCX
from util.generatePDF import generatePDF
from util.generatePNG import generatePNG
from util.generateCSV import generateCSV
from util.generateJPG import generateJPEG
from util.generateXLSX import generateXLSX
from util.randomObjectName import listRandomObjectNames

def generateFiles(fileNamePrefix, extensions, filesizes, path, baseDir, numFiles, offset = 0, debug=False):
    names = listRandomObjectNames(numFiles, offset)
    for i in range(numFiles):
        if extensions[i] == ".txt":
            generateTXT(fileNamePrefix, filesizes[i], path, baseDir, names[i])
        if extensions[i] == ".docx":
            generateDOCX(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
        if extensions[i] == ".pdf":
            generatePDF(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
        if extensions[i] == ".png":
            generatePNG(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
        if extensions[i] == ".jpg":
            generateJPEG(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
        if extensions[i] == ".csv":
            generateCSV(fileNamePrefix, filesizes[i], path, baseDir, names[i])
        if extensions[i] == ".xlsx":
            generateXLSX(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)