# Input
#   file prefix, if not specify randomly generated
#   file size, if not specify default 2KB
#   destination path
#   base directory

# Output
#   {destinationPath}/TXTFile.txt

# import os
from util.randomObjectName import randomObjectName
import logging
logger = logging.getLogger(__name__)

def generateTXT(filePrefix: str, fileSize: int, destinationPath, baseDir, name=None):
    extension = ".txt"
    lorem_path = f"{baseDir}/resources/loremIpsum.txt"
    # lorem_size = os.path.getsize(lorem_path)
    # print(str(lorem_size))
    with open(lorem_path, "r") as loremfile:
        # Creates string to write into output
        # lorem is 1 KB
        lorem = loremfile.read(1024)
    
    # GenerateFileName
    fileName = ""
    if filePrefix is not None:
        fileName += str(filePrefix) + "_"
    if not name:
        fileName += randomObjectName()
    else:
        fileName += name
    fileName += ".txt"

    # Generate Path
    path = ""
    if destinationPath is not None:
        path += destinationPath
        if path[:-1] != '/':
            path += "/"
    else:
        path += f"{baseDir}/output/"
    path += fileName
    
    loops = int(fileSize/1024)
    # Writes into output to make output the specified size
    with open(path, "w") as output:
        for i in range(loops):
            output.write(lorem)
    print(f"Generated {path}")
    logger.info(f"Generated {path}")