#!/usr/bin/python3
import sys
from util.generateManifest import generateManifest

def main():
    if len(sys.argv) < 2:
        print("ERROR: Missing Path")
    else:
        generateManifest(sys.argv[1])

if __name__ == "__main__":
    main()