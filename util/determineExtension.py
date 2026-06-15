import random
import logging
from datetime import datetime
logger = logging.getLogger(__name__)

def generateListExtensions(fileSizes, numFiles: int, debug=False):
    random.seed(int(datetime.now().timestamp()))
    extensions = []
    for i in range(numFiles):
        fileSize = fileSizes[i]
        if debug: 
            print(f"File Size: {fileSize}")
            logger.info(f"File Size: {fileSize}")
        extensions.append(determineExtension(fileSize))
    return extensions

def determineExtension(size: int):
    extensions = [".png", ".txt", ".csv", ".jpg", ".pdf", ".xlsx", ".docx"]

    extensionIndex = 0

    minDocxSize = 38000;
    maxPngSize = 1000000

    # 38000 aprox min of .docx
    if size < minDocxSize:
        extensionIndex = random.randint(0, 5)
    # PNG generation is really slow past 1 MB
    elif size > maxPngSize: 
        extensionIndex = random.randint(1, 6)
    else:
        extensionIndex = random.randint(0, 6)

    return extensions[extensionIndex]