import sys

ACTIVE_CLASS = "headerActive"

with open(sys.argv[2]) as f:
    template = f.read()

actDict = {}

actDict["about"] = ""
actDict["findus"] = ""
actDict["home"] = ""
actDict["officers"] = ""
actDict["photos"] = ""

actDict[sys.argv[1]] = ACTIVE_CLASS

print(template.format(about = actDict["about"], findus = actDict["findus"], home = actDict["home"], officers = actDict["officers"], photos = actDict["photos"]))
