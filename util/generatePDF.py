# Input
#   file prefix, if not specify randomly generated
#   file size, if not specify default 2KB
#   destination path

# Output
#   PDFFile
from fpdf import FPDF
from util.randomObjectName import randomObjectName
import os
import logging
logger = logging.getLogger(__name__)

def generatePDF(filePrefix, fileSize: int, destinationPath, baseDir, name=None, debug=False):
    extension = ".pdf"
    lorem_path = f"{baseDir}/resources/loremIpsum.txt"

    loremSize = 2733

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

    # Default pdf size is 909
    pdf = FPDF(orientation="P", unit="mm", format="Letter")

    pdf.add_page()

    # 3. Set your font (Core fonts: Helvetica, Arial, Times, Courier)
    pdf.set_font("Helvetica", style="B", size=16)

    # 4. Create a text cell (Width, Height, Text, Border, NewLine, Alignment)
    # pdf.cell(w=0, h=10, text="Hello, World!", border=0, ln=1, align="C")
    pdf.cell(w=0, h=10, text=fileName[:-4], border=0, align="C")

    # # 5. Add body text with smaller font
    # pdf.set_font("Helvetica", style="", size=12)
    # pdf.ln(5)  # Add a line break spacing of 5mm
    # pdf.cell(w=0, h=10, text="This PDF was generated programmatically using Python and fpdf2.", ln=1)

    size = 1007
    while size < fileSize - 2700:
        pdf.multi_cell(w=190, h=10, text=lorem, border=1, align='L')
        size += 2700
        if debug:
            print(f"Generating {fileName} | Expected size: {fileSize} | Current approximate size: {size}")
            logger.info(f"Generating {fileName} | Expected size: {fileSize} | Current approximate size: {size}")
    pdf.output(path)
    size = os.path.getsize(path)
    print(f"PDF size: {size}")
    logger.info(f"PDF size: {size}")

    # 6. Save the final file
    print(f"Generated {path}")
    logger.info(f"Generated {path}")