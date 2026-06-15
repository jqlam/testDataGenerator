import logging
from datetime import datetime
import sys
from pathlib import Path
from util.generateTXT import generateTXT
from util.generateDOCX import generateDOCX
from util.generatePDF import generatePDF
from util.generatePNG import generatePNG
from util.generateCSV import generateCSV
from util.generateJPG import generateJPEG
from util.generateXLSX import generateXLSX
from util.randomObjectName import randomObjectName
from util.determineExtension import generateListExtensions
from util.generateFileSizes import generateFileSizes
from util.generateFile import generateFiles
from processor.generator_settings import GeneratorSettings

class GeneratorData:
    def __init__(self, settings: GeneratorSettings):
        self._DIRECTORY_DEPTH = int(settings.DIRECTORY_DEPTH)
        self._TOTAL_FILE_COUNT = int(settings.TOTAL_FILE_COUNT)
        self._MIN_FILE_SIZE = settings.MIN_FILE_SIZE
        self._MAX_FILE_SIZE = settings.MAX_FILE_SIZE
        self._ROOT_DIRECTORY_NAME = settings.ROOT_DIRECTORY_NAME
        self._FILE_NAME_PREFIX = settings.FILE_NAME_PREFIX
        self._BASE_DIR = settings.BASE_DIR
        self._CURRENT_LEVEL = 1
        self._OUTPUT_DESTINATION = "output"
        self.logger = logging.getLogger(__name__)

    #------------------------------------------------
    # def _generateFile(self, extension, filesize, path):
    #     if extension == ".txt":
    #         generateTXT(self._FILE_NAME_PREFIX, filesize, path, self._BASE_DIR)
    #     if extension == ".docx":
    #         generateDOCX(self._FILE_NAME_PREFIX, filesize, path, self._BASE_DIR)
    #     if extension == ".pdf":
    #         generatePDF(self._FILE_NAME_PREFIX, filesize, path, self._BASE_DIR)
    #     if extension == ".png":
    #         generatePNG(self._FILE_NAME_PREFIX, filesize, path, self._BASE_DIR)
    #     if extension == ".jpg":
    #         generateJPEG(self._FILE_NAME_PREFIX, filesize, path, self._BASE_DIR)
    #     if extension == ".csv":
    #         generateCSV(self._FILE_NAME_PREFIX, filesize, path, self._BASE_DIR)
    #     if extension == ".xlsx":
    #         generateXLSX(self._FILE_NAME_PREFIX, filesize, path, self._BASE_DIR)

    #------------------------------------------------
    def _createDirectory(self):
        invoker = self.__class__.__name__ + "." +  sys._getframe().f_code.co_name
        now = datetime.now()
    
        print (f"\n\n{now} BEGIN: {invoker}")
        self.logger.info(f"\n\n{now} BEGIN: {invoker}")

        if not self._ROOT_DIRECTORY_NAME:
            self._ROOT_DIRECTORY_NAME = randomObjectName()
        
        directoryPath = f"{self._OUTPUT_DESTINATION}/{self._ROOT_DIRECTORY_NAME}"
        if self._CURRENT_LEVEL >= 2:
            for i in range(2, self._CURRENT_LEVEL + 1):
                directoryPath += f"/{self._ROOT_DIRECTORY_NAME}_{i:02}"
                print(directoryPath)

        directory = Path(directoryPath)
        directory.mkdir(parents=True, exist_ok=True)
        print(f"DIRECTORY {directoryPath} CREATED")
        self.logger.info(f"DIRECTORY {directoryPath} CREATED")
        self._CURRENT_LEVEL += 1

        print (f"\n\n{now} END: {invoker}")
        self.logger.info(f"\n\n{now} END: {invoker}")

        return directoryPath

    #------------------------------------------------
    def _createDirectoryHierarchy(self, fileCountPerLevel, extensions, fileSizes):
        invoker = self.__class__.__name__ + "." +  sys._getframe().f_code.co_name
        now = datetime.now()
    
        print (f"\n\n{now} BEGIN: {invoker}")
        self.logger.info(f"\n\n{now} BEGIN: {invoker}")

        if self._ROOT_DIRECTORY_NAME:
            if self._preexistingDirectory():
                return False
            elif self._ROOT_DIRECTORY_NAME == "":
                self._ROOT_DIRECTORY_NAME = randomObjectName()
        else:
            self._ROOT_DIRECTORY_NAME = randomObjectName()

        # create nested directories
        index = 0
        print(f"File Extension Order: {extensions}")
        self.logger.info(f"File Extension Order: {extensions}")
        for i in range(self._DIRECTORY_DEPTH):
            nextIndex = index + fileCountPerLevel[i]
            offset = (i+1) * 100 # Arbitrary Offset to guarantee differnt file names
            directoryPath = self._createDirectory()
            generateFiles(self._FILE_NAME_PREFIX, extensions[index:nextIndex], fileSizes[index:nextIndex], 
                          directoryPath, self._BASE_DIR, fileCountPerLevel[i], offset, debug=True)
            index = nextIndex

        print (f"\n\n{now} END: {invoker}")
        self.logger.info(f"\n\n{now} END: {invoker}")
        return True

    #------------------------------------------------
    # Create Array to determine the number of files generated on each level
    def _computeLevelFileCount(self):
        base = int(self._TOTAL_FILE_COUNT/self._DIRECTORY_DEPTH)
        remainder = int(self._TOTAL_FILE_COUNT%self._DIRECTORY_DEPTH)
        filesPerLevel = []
        for i in range(self._DIRECTORY_DEPTH):
            if i == 0:
                filesPerLevel.append(base + remainder)
            else:
                filesPerLevel.append(base)
        return filesPerLevel
    
    #------------------------------------------------
    # Determine if the directory path already exists
    def _preexistingDirectory(self):
        # print("entered _prexistingDirectory")
        path = Path(f"{self._OUTPUT_DESTINATION}/{self._ROOT_DIRECTORY_NAME}")
        if path.exists():
            print(f"{path} already exists.")
            self.logger.info(f"{path} already exists.")
            return True
        return False
    

    #------------------------------------------------
    def generate(self):
        invoker = self.__class__.__name__ + "." +  sys._getframe().f_code.co_name
        now = datetime.now()
    
        print (f"\n\n{now} BEGIN: {invoker}")
        self.logger.info(f"\n\n{now} BEGIN: {invoker}")

        fileSizes = generateFileSizes(self._MIN_FILE_SIZE, self._MAX_FILE_SIZE, self._TOTAL_FILE_COUNT)
        extensions = generateListExtensions(fileSizes, self._TOTAL_FILE_COUNT)

        # Create Array to determine the number of files generated on each level
        fileCountPerLevel = self._computeLevelFileCount()

        if not self._createDirectoryHierarchy(fileCountPerLevel, extensions, fileSizes):
            print (f"\n\n{now} END: {invoker}")
            self.logger.info(f"\n\n{now} END: {invoker}")
            return

        print (f"\n\n{now} END: {invoker}")
        self.logger.info(f"\n\n{now} END: {invoker}")