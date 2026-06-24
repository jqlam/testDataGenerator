<!-- For Word implementation: pip install python-docx
    sudo apt update
    sudo apt install python3-pip python3-venv -y
    pip3 install python-docx
Note:(Note: If Ubuntu blocks the global pip installation 
    due to an externally managed environment, run 
    python3 -m venv venv && source venv/bin/activate 
    first, then run pip install python-docx).

     
  cd summer2026/TestDataGenerator/
  python3 -m venv venv && source venv/bin/activate
  pip install python-docx
  deactivate

Word doc must be > 36 KB

pip install pandas openpyxl
pip install python-docx
pip install fpdf2
pip install Pillow
pip install deepdiff -->

# README
This program will generate random dummy files for testing purposes. It will generate any number of files roughly split up among a specified amount of levels of directories as well as a manifest file. Outputs may be adjusted by changing the options file. The files generated will be one of six types: TXT, CSV, DOCX, XLSX, PDF, PNG, JPG. File generation may take varied amounts of time depending on which types of files.

Command to run: ```./generateTestData.py test_data_generator_settings.json```

Options file: test_data_generator_settings.json
Contains 4 required fields and 2 optional fields
#### REQUIRED:
- DIRECTORY_DEPTH 
    - determines how many layers of directories the files will be generated in
- TOTAL_FILE_COUNT 
    - determines the amount of files to be generated
- MIN_FILE_SIZE 
    - the smallest a file you want generated will be
- MAX_FILE_SIZE 
    - the largest a file you want generated will be
- note: file sizes should be in the format (number size) - ex. 10 KB. Can be in KB, MB, and GB

#### OPTIONAL:
- ROOT_DIRECTORY_NAME 
    - Changes what the output root directory will be named (WILL FAIL IF DIRECTORY ALREADY EXISTS)
- FILE_NAME_PREFIX 
    - A string that will be prepended in front of the randomly generated file names

**Other notes:**
- .docx (Word Documents) must be at least 38 KB
- .png (Image) will not be bigger than 1 MB

### Manifest File
The program will generate a manifest file upon running the code (which is an xlsx file that shows information about the files in the directory that was generated). You may also generate a manifest file for a preexisisting by running ```./manifestGenerator.py [INSERT DIRECTORY NAME HERE]``` in the main directory.

The program can also check the differences between two existing manifest files using the command ```./ManifestDiff.py [ManifestFile1] [ManifestFile2]```

### Log File
While generating the files, the program will keep track of its progress in a log file that can be found in the log directory . If the log directory does not exist, the program will make one and then save the file there.