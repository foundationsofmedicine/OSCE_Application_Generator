import os
import pandas as pd

def generatePublicFolderStructure():
    # Generate the basic folder structures
    generateFolder("./public")
    return

def retrieveOSCElist():
    osce_map = pd.read_csv("./src/osce_map.csv")
    OSCElist = osce_map['OSCE_ID'].tolist()
    OSCElist = [str(item) for item in OSCElist] # convert whatever text or numerical values into a string
    return OSCElist

def generateOSCEFolders():
    OSCElist = retrieveOSCElist()
    for item in OSCElist:
        generateFolder("./public/" + item)
        generateFolder("./public/" + item + "/prompt")
        generateFolder("./public/" + item + "/actor_prompt")
    return

def generateFolder(location):
    if not os.path.isdir(location):
        os.mkdir(location)
        print ("New folder generated at " + location)
    else:
        print ("Folder already exists at " + location)
    return