# Input
#   a string with a format: a number + KB/MB/GB
# Output
#   bytes
#   if improper unit, return 0
import re

def getBytes(rawSize, debug=False):
    num = ""
    unit = ""

    # text = "10 kB"
    num, unit = re.findall(r'\D+|\d+', rawSize)
    unit = unit.strip().upper()
    if debug:
        print(num, unit)
    num = int(num)
    
    ##Convert to Bytes
    match unit:
        case "KB":
            num = num * 1024
        case "MB":
            num = num * 1024 * 1024
        case "GB":
            num = num * 1024 * 1024 * 1024
        case _:
            num = 0

    if debug:
        print(str(num))
    return num