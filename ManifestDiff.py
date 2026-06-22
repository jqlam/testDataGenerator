#!/usr/bin/python3

# python3 -m venv .venv
# source .venv/bin/activate
# pip install pipreqs
# pip install deepdiff
# deactivate

import sys
import pandas as pd
from deepdiff import DeepDiff

def _manifestDiff(manifest1: str, manifest2: str, debug = False):
    file1 = pd.read_excel(manifest1) 
    file2 = pd.read_excel(manifest2)

    dict1 = file1.to_dict(orient='records')
    dict2 = file2.to_dict(orient='records')

    # Find the semantic differences regardless of element ordering
    difference = DeepDiff(dict1, dict2, ignore_order=True)

    #print(difference)
    if debug:
        print(difference.pretty())

    print(f"Manifest 1 = {manifest1}")
    print(f"Manifest 2 = {manifest2}")

    if not difference:
        print ("Manifest 1 = Manifest 2")
    else:
        print ("Manifest 1 != Manifest 2")

def main():
    if len(sys.argv) < 3:
        print("ERROR: MISSING INPUTS")
    else:
        if len(sys.argv) > 3:
            _manifestDiff(sys.argv[1], sys.argv[2], sys.argv[3])
        else:
            _manifestDiff(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()