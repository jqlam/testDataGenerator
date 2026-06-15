from datetime import datetime
import sys
import os
import json
import logging
logger = logging.getLogger(__name__)

class GeneratorSettings:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self._load_settings()
        self.logger = logging.getLogger(__name__)

    def _load_settings(self):
        invoker = self.__class__.__name__ + "." +  sys._getframe().f_code.co_name
        now = datetime.now()    
        print (f"\n\n{now} BEGIN: {invoker}")  
        logger.info(f"\n\n{now} BEGIN: {invoker}")      

        try:
            with open(self.input_file, 'r') as file:
                data_dict =json.load(file)

                for key, value in data_dict.items():
                    clean_key = key.strip().lower().replace(' ', '_').upper()

                    # set attribute dynamically using setattr
                    setattr(self, clean_key, value)

            # add base directory to settings
            baseDir = os.getcwd() + "/"
            setattr(self, "BASE_DIR", baseDir)

            now = datetime.now()
            print (f"{now} END: {invoker}")
            logger.info(f"{now} END: {invoker}")

        except FileNotFoundError:
            print (f"ERROR: {self.input_file} not found")
            logger.info(f"ERROR: {self.input_file} not found")