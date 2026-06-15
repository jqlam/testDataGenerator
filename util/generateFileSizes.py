import random
from datetime import datetime
from util.getBytes import getBytes
import logging
logger = logging.getLogger(__name__)

def generateFileSizes(MinFileSize, MaxFileSize, numFiles, debug=False):
    random.seed(int(datetime.now().timestamp()))
    fileSizes = []
    for i in range(numFiles):
        fileSizes.append(random.randint(getBytes(MinFileSize), getBytes(MaxFileSize)))
    if debug:
        print(f"File Sizes: {fileSizes}")
        logger.info(f"File Sizes: {fileSizes}")
    return fileSizes