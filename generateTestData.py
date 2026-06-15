#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path

from processor.generator_settings import GeneratorSettings
from processor.generator_data import GeneratorData

import sys
import logging
logger = logging.getLogger(__name__)

#------------------------------------------------
def process():
    invoker = sys._getframe().f_code.co_name
    now = datetime.now()
    print (f"\n\n{now} BEGIN: {invoker}")
    logger.info(f"\n\n{now} BEGIN: {invoker}")

    if len(sys.argv) < 2:
        print ("ERROR: missing input file")
        print ("Usage: python3 script.py <filename>")
        sys.exit(1)

    i_file = sys.argv[1]

    print (f"INPUT_FILE_NAME: '{i_file}'")
    i_file_path = Path(i_file);
    print (f"INPUT_FILE_PATH: '{i_file_path}'")

    if i_file_path.is_file():
        # get settings
        settings = GeneratorSettings(i_file_path)
        for key, value in settings.__dict__.items():
                print(f"{key} -> {value}")
        
        data = GeneratorData(settings)
        data.generate()

    else:
        print (f"ERROR: input file '{i_file_path}' not found")

    now = datetime.now()
    print (f"\n\n{now} END: {invoker}")
    logger.info(f"\n\n{now} END: {invoker}")

#------------------------------------------------
def main():
    invoker = sys._getframe().f_code.co_name
    now = datetime.now()
    loggerFileName = f"generateTestData-{now.strftime("%Y%m%d%H%M%S")}.log"
    logging.basicConfig(filename=loggerFileName, level=logging.INFO)
    print (f"{now} BEGIN: {invoker}")
    logging.info(f"{now} BEGIN: {invoker}")

    process()

    now = datetime.now()
    print (f"\n\n{now} END: {invoker}")
    logging.info(f"\n\n{now} END: {invoker}")
    sys.exit(0)

if __name__ == "__main__":
    main()