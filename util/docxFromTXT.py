# Input
#   file prefix, if not specify randomly generated
#   file size, if not specify default 2KB
#   destination path

# Output
#   DOCXFile

#from docx import Document
from docx import Document
from util.generateTXT import generateTXT
from util.randomObjectName import randomObjectName
import logging
import os
logger = logging.getLogger(__name__)

def generateTXTDOCX(filePrefix, fileSize, destinationPath, baseDir, name=None, debug=False):
    extension = ".docx"
    lorem_path = f"{baseDir}/resources/loremIpsum.txt"

    loremSize = 2733
    baseSize = 36563 #The smallest size a word doc can be
    size = fileSize - baseSize

    with open(lorem_path, "r") as loremfile:
        # Creates string to write into output
        # lorem is 1 KB
        lorem = loremfile.read()
        loremRemainder = loremfile.read((size * 2)%loremSize)
    
    # GenerateFileName
    fileName = ""
    if filePrefix is not None:
        fileName += str(filePrefix) + "_"
    if not name:
        fileName += randomObjectName()
    else:
        fileName += name
    fileName += extension

    # Generate Path
    path = ""
    if destinationPath is not None:
        path += destinationPath
        if path[:-1] != '/':
            path += "/"
    else:
        path += f"{baseDir}/output/"
    path += fileName

    # Generate TempTXT
    generateTXT(None, fileSize, "resources", baseDir, fileName[:-5], utility=True)

    # Add a standard text paragraph
    doc = Document()
    doc.add_heading(fileName[:-5], 0)

    with open(f"resources/{fileName[:-5]}.txt", "r") as text:
        content = text.read()
    doc.add_paragraph(content)
    doc.save(path)

    size = os.path.getsize(path)
    textSize = size - baseSize
    while size < fileSize:
        difference = fileSize - size
        textSize = size - baseSize
        loops = int(difference/textSize)
        if loops < 1: loops = 1
        for i in range(loops):
            doc.add_paragraph(content)
        doc.save(path)
        size = os.path.getsize(path)
        if debug:
            print(f"Genererating {fileName} | Expected size: {fileSize} | Current Size: {size}")
            logger.info(f"Genererating {fileName} | Expected size: {fileSize} | Current Size: {size}")

    os.remove(f"resources/{fileName[:-5]}.txt")
    print(f"Generated {path}")
    logger.info(f"Generated {path}")