import os
import random
import pytest
from util.generateTXT import generateTXT
from util.getBytes import getBytes
from util.randomObjectName import randomObjectName
from util.generateDOCX import generateDOCX
from util.generatePDF import generatePDF
from util.generatePNG import generatePNG
from util.generateCSV import generateCSV
from util.generateJPG import generateJPEG
from util.generateXLSX import generateXLSX
from util.determineExtension import determineExtension
from util.determineExtension import generateListExtensions
from util.docxFromTXT import generateTXTDOCX
from datetime import datetime

def main():
    now = datetime.now()
    print (f"\n\n{now} BEGIN: Testing")
    random.seed(1)
    baseDir = os.getcwd()

    print(baseDir)
   
    # generateTXT(None, 10000000, "output", baseDir)
    # getBytes("1 gb")
    # generateDOCX("Case_02", 10000000, "output", baseDir, debug=True)
    generateTXTDOCX("Case_02", 10000000, "output", baseDir, debug=True)
    # generatePDF("Case_02", 900000, "output/output1", baseDir, debug=True)
    # generatePNG("Case_03", 900000, "output/output1", baseDir, debug=True)
    # generateCSV("Case_04", "10 kB", None)
    # generateJPEG("Case01", 900000, "output/output1", baseDir, debug=True)
    # generateXLSX("Case_03", 10000000, "output/output1", baseDir, debug=True)
    # TESTXLSX("TEST", 10000000, "output", baseDir, debug=True)
    # print(generateListExtensions(3000, 38000, 7))
    now = datetime.now()
    print (f"\n\n{now} END: Testing")

if __name__ == "__main__":
    main()