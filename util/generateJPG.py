from PIL import Image, ImageDraw
from util.randomObjectName import randomObjectName
import random
import os
import math
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

def generateJPEG(filePrefix, fileSize, destinationPath, baseDir, name=None, debug=False):
    extension = ".jpg"
    fileFormat = "JPEG" 
    
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

     # To adjust the canvas based on the desired file size
    sizeReduce = 4
    fileSizeTemp = fileSize
    while fileSizeTemp > 10:
        fileSizeTemp /= 10
        sizeReduce *= 2
    # Canvas size based on desired file size
    # print(sizeReduce)
    x = int(fileSize/sizeReduce)
    y = int(fileSize/sizeReduce)

    # Create a new RGB image with a blue background (width=400, height=300)
    random.seed(int(datetime.now().timestamp()))
    img = Image.new("RGB", (x, y), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # Initialize a drawing canvas
    canvas = ImageDraw.Draw(img)
    img.save(path, fileFormat)
    size = os.path.getsize(path)
    # print(size)
    prevSize = 0
    while (size < fileSize):
        x0 = random.randint(0, int(x * 0.9))
        y0 = random.randint(0, int(y * 0.9))
        x1 = random.randint(x0, x)
        y1 = random.randint(y0, y)
        canvas.rectangle([x0, y0, x1, y1], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        img.save(path, fileFormat)
        prevSize = size
        size = os.path.getsize(path)
        if debug:
            print(f"Generating {fileName} | Expected size: {fileSize} | Current file size: {size}")
            logger.info(f"Generating {fileName} | Expected size: {fileSize} | Current file size: {size}")
        # Resize the canvas to increase the file size
        if prevSize > size:
            x += 20 * int(math.log2(sizeReduce))
            y += 20 * int(math.log2(sizeReduce))
            newSize = (x, y)
            img = img.resize(newSize, resample=Image.Resampling.LANCZOS)
            img.save(path, fileFormat)
            size = os.path.getsize(path)
            if debug:
                print(f"Canvas has been resized | Expected size: {fileSize} | Current file size: {size}")
                logger.info(f"Canvas has been resized | Expected size: {fileSize} | Current file size: {size}")
            canvas = ImageDraw.Draw(img)
    
    # img.save("/mnt/c/transfer/output_pillow.jpg", "JPEG")
    print(f"Generated {path}")
    logger.info(f"Generated {path}")
