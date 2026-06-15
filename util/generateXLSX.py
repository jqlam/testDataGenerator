# Input
#   file prefix, if not specify randomly generated
#   file size, if not specify default 2KB
#   destination path

# Output
#   XLSXFile

import pandas as pd
import os
import logging
from util.randomObjectName import randomObjectName
logger = logging.getLogger(__name__)

def generateXLSX(filePrefix, fileSize, destinationPath, baseDir, name=None, debug=False):
    extension = ".xlsx"
    lorem_path = f"{baseDir}/resources/loremIpsum.txt"
    with open(lorem_path, "r") as loremfile:
            # Creates string to write into output
            # lorem is 1 KB
            lorem = loremfile.read()

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

    splitLorem = lorem.split()
    data = {}
    # for i in range(len(splitLorem)):
    #     data.update({splitLorem[i]: splitLorem})
    data.update({"Lorem": splitLorem})

    df = pd.DataFrame(data)

    totalRows = len(df)
    
    df.to_excel(path, index=False)
    size = os.path.getsize(path)
    prevSize = 0
    difference = 0
    i = 0
    rowByte = 1060
    while size < fileSize - rowByte:
        # print(f"Current Doc Size: {size}")
        df[f"bloat_col_{i}"] = splitLorem
        i += 1
        df.to_excel(path, index=False)
        prevSize = size
        size = os.path.getsize(path)
        difference = size - prevSize
        if size < fileSize:
            loops = int(((fileSize)-size)/difference)
            for j in range(loops):
                df[f"bloat_col_{i}"] = splitLorem
                i += 1
            df.to_excel(path, index=False)
            size = os.path.getsize(path)
        if debug:
            print(f"Generating {fileName} | Expected file size: {fileSize} | Current size: {size}")
            logger.info(f"Generating {fileName} | Expected file size: {fileSize} | Current size: {size}")

    print(f"Generated {path}")
    logger.info(f"Generated {path}")