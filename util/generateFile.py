from util.generateTXT import generateTXT
from util.generateDOCX import generateDOCX
from util.docxFromTXT import generateTXTDOCX
from util.generatePDF import generatePDF
from util.generatePNG import generatePNG
from util.generateCSV import generateCSV
from util.generateJPG import generateJPEG
from util.generateXLSX import generateXLSX
from util.generateZIP import generateZIP
from util.randomObjectName import listRandomObjectNames

def generateFiles(fileNamePrefix, extensions, filesizes, path, baseDir, numFiles, offset = 0, debug=False):
    names = listRandomObjectNames(numFiles, offset)
    for i in range(numFiles):
        if extensions[i] == ".txt":
            generateTXT(fileNamePrefix, filesizes[i], path, baseDir, names[i])
        if extensions[i] == ".docx":
            # generateDOCX(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
            if filesizes[i] > 1000000:
                generateTXTDOCX(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
            else:
                generateZIP(fileNamePrefix, filesizes[i], path, baseDir, "docx", names[i], debug)
        if extensions[i] == ".pdf":
            if filesizes[i] > 1000000:
                generatePDF(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
            else:
                generateZIP(fileNamePrefix, filesizes[i], path, baseDir, "pdf", names[i], debug)
        if extensions[i] == ".png":
            if filesizes[i] > 1000000:
                generatePNG(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
            else:
                generateZIP(fileNamePrefix, filesizes[i], path, baseDir, "png", names[i], debug)
        if extensions[i] == ".jpg":
            if filesizes[i] > 1000000:
                generateJPEG(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
            else:
                generateZIP(fileNamePrefix, filesizes[i], path, baseDir, "jpg", names[i], debug)
        if extensions[i] == ".csv":
            generateCSV(fileNamePrefix, filesizes[i], path, baseDir, names[i])
        if extensions[i] == ".xlsx":
            if filesizes[i] > 1000000:
                generateXLSX(fileNamePrefix, filesizes[i], path, baseDir, names[i], debug)
            else:
                generateZIP(fileNamePrefix, filesizes[i], path, baseDir, ".xlsx", names[i], debug)