from PIL import Image, ImageDraw
from datetime import datetime
from util.randomObjectName import randomObjectName
import random
import os
import math
import logging
logger = logging.getLogger(__name__)

def generatePNG(filePrefix, fileSize: int, destinationPath, baseDir, name=None, debug=False):
    extension = ".png"
    fileFormat = "PNG"

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
    sizeReduce = 1
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
    while (size < fileSize - 4000):
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
                print(f"Canvas has been resized | Expected size: {fileSize} | Current size: {size}")
                logger.info(f"Canvas has been resized | Expected size: {fileSize} | Current size: {size}")
            canvas = ImageDraw.Draw(img)
        # print(f"Current File Size: {size}")
    
    # if (prevSize > size):
    #     # while (size < fileSize * 0.92):
    #     noise_mask = Image.effect_noise(img.size, 1)
    #     img = Image.blend(img, noise_mask.convert("RGB"), 0.01)
    #     img.save(path, fileFormat)
    #     size = os.path.getsize(path)
    #     print(f"Current File Size: {size}")

    #img.save("/mnt/c/transfer/output_pillow.png", "PNG")
    print(f"Generated {path}")
    logger.info(f"Generated {path}")
