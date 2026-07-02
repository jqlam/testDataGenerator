# README
This program will generate random dummy files for testing purposes. It will generate any number of files roughly split up among a specified amount of levels of directories as well as a manifest file. Outputs may be adjusted by changing the options file. The files generated will be one of six types: TXT, CSV, DOCX, XLSX, PDF, PNG, JPG. File generation may take varied amounts of time depending on which types of files.

#### SET UP:
If you do not have the virtual enviornment (venv) set up, then run the command ```./setup-venv.sh``` to set up and install the required libraries. Otherwise, just activate the virtual environment with ```source .venv/bin/activate```.

When you are finished running the program, deactivate the virtual environment with ```deactivate```.

#### RUNNING THE PROGRAM
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
- note: file sizes should be in the format (number size) - ex. 10 KB. Can be in KB, MB, and GB. Generation speed also tends to slow down the bigger the file is i.e. 10 MB would take a while for certain file types.

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