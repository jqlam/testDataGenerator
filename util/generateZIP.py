import zipfile
import os
import shutil
from pathlib import Path
from util.randomObjectName import randomObjectName
from util.generateTXT import generateTXT
from util.generateDOCX import generateDOCX
from util.docxFromTXT import generateTXTDOCX
from util.generatePDF import generatePDF
from util.generatePNG import generatePNG
from util.generateCSV import generateCSV
from util.generateJPG import generateJPEG
from util.generateXLSX import generateXLSX

def generateZIP(filePrefix, fileSize: int, destinationPath, baseDir, fileType, name=None, debug=False):
    extension = ".zip"
    fileName = ""
    if filePrefix is not None:
        fileName += str(filePrefix) + "_"
    if not name:
        fileName += randomObjectName()
    else:
        fileName += name
    # fileName += extension

    # Generate Path
    path = ""
    if destinationPath is not None:
        path += destinationPath
        if path[:-1] != '/':
            path += "/"
    else:
        path += f"{baseDir}/output/"
    path += fileName

    numFiles = 1
    smallerFileSize = fileSize
    while smallerFileSize > 1000000:
        numFiles *= 2
        smallerFileSize /= 2
    smallerFileSize = int(smallerFileSize)
    if debug:
        print(f"Number of files: {numFiles}")
        print(f"Size of files: {smallerFileSize}")
    prependingZero = 1
    numFileTemp = numFiles
    while numFileTemp > 9:
        prependingZero += 1
        numFileTemp /= 10

    # Create a temporary directory to make files to zip up
    tempPath = f"{baseDir}/resources/{fileName[:-4]}"
    if debug:
        print("Created temporary directory")
    os.makedirs(tempPath, exist_ok=True)
    
    for i in range(numFiles):
        if debug:
            print(f"Generating file {i+1}/{numFiles}")
        if fileType == "docx":
            generateTXTDOCX(filePrefix, smallerFileSize, tempPath, baseDir, name=f"{fileName}_{i+1:0{prependingZero}}")
        if fileType == "xlsx":
            generateXLSX(filePrefix, smallerFileSize, tempPath, baseDir, name=f"{fileName}_{i+1:0{prependingZero}}")
        if fileType == "pdf":
            generatePDF(filePrefix, smallerFileSize, tempPath, baseDir, name=f"{fileName}_{i+1:0{prependingZero}}")
        if fileType == "png":
            generatePNG(filePrefix, smallerFileSize, tempPath, baseDir, name=f"{fileName}_{i+1:0{prependingZero}}")
        if fileType == "jpg":
            generateJPEG(filePrefix, smallerFileSize, tempPath, baseDir, name=f"{fileName}_{i+1:0{prependingZero}}")

    shutil.make_archive(path, "zip", tempPath)
    # Figure out if the zip file should be a certain size or if the contents should total to that size

    shutil.rmtree(tempPath)