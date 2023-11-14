# Author: NAS
# Date: 2023-11-05
import os
import datetime


def moveFile(origFilePath, newFilePath): 
    try:
        os.replace(origFilePath, newFilePath)
        print("Source path renamed to destination path successfully.")
    
    # If Source is a file
    # but destination is a directory
    except IsADirectoryError:
        print("Source is a file but destination is a directory.")
    
    # If source is a directory
    # but destination is a file
    except NotADirectoryError:
        print("Source is a directory but destination is a file.")
    
    # For permission related errors
    except PermissionError:
        print("Operation not permitted.")
    
    # For other errors
    except OSError as error:
        print("Other Error.")


def readFile(file, fileName, vaultPath): 
    with open(file) as fp:
        for index, line in enumerate(fp):
            _type = ""
            subtype = ""
            if "type:" in line.strip() and "subtype" not in line.strip(): 
                arr = line.strip().split(": ")  
                _type = arr[1]
                if arr[1] == "person": 
                    moveFile(file, vaultPath + "/People/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "movie": 
                    moveFile(file, vaultPath + "/MoviesTV/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "tvseason": 
                    moveFile(file, vaultPath + "/MoviesTV/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "tvshow": 
                    moveFile(file, vaultPath + "/MoviesTV/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "movieSeries": 
                    moveFile(file, vaultPath + "/MoviesTV/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "tvepisode": 
                    moveFile(file, vaultPath + "/MoviesTV/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "event": 
                    moveFile(file, vaultPath + "/Events/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "BibleBooks": 
                    moveFile(file, vaultPath + "/Writing/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "quote": 
                    moveFile(file, vaultPath + "/Writing/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "correspondence": 
                    moveFile(file, vaultPath + "/Writing/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "videoSeries": 
                    moveFile(file, vaultPath + "/Writing/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "weekly": 
                    moveFile(file, vaultPath + "/Weeklies/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "daily": 
                    moveFile(file, vaultPath + "/Dailies/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "HQ": 
                    moveFile(file, vaultPath + "/Misc/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "BizIdea": 
                    moveFile(file, vaultPath + "/Work/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "money": 
                    moveFile(file, vaultPath + "/Money/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "recipe": 
                    moveFile(file, vaultPath + "/Recipes/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "ProSportsTeam": 
                    moveFile(file, vaultPath + "/Sports/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "sportsNote": 
                    moveFile(file, vaultPath + "/Sports/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "bill": 
                    moveFile(file, vaultPath + "/Money/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "budgetPlan": 
                    moveFile(file, vaultPath + "/Money/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "paycheckPlan": 
                    moveFile(file, vaultPath + "/Money/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "organization": 
                    moveFile(file, vaultPath + "/Organizations/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "goal": 
                    moveFile(file, vaultPath + "/Tasks/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "book": 
                    moveFile(file, vaultPath + "/Books/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "bookSeries": 
                    moveFile(file, vaultPath + "/Books/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "testArea": 
                    moveFile(file, vaultPath + "/Misc/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "presents": 
                    moveFile(file, vaultPath + "/Misc/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "game": 
                    moveFile(file, vaultPath + "/Misc/" + fileName)
                    print("moved: " + fileName)
                    
                    
                else: 
                    print("type not processed yet - " + arr[1])
                # match arr[1]: 
                #     case "person": 
                #         print("PERSON - Move it!")
                #     case "movie": 
                #         print("Movie")
                #     case _:
                #         print("type not processed yet - " + arr[1])
            # end if 

            if "subtype:" in line.strip():  
                arr = line.strip().split(": ")  
                subtype = arr[1] 
                if arr[1] == "daily": 
                    moveFile(file, vaultPath + "/Dailies/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "organizationNote": 
                    moveFile(file, vaultPath + "/Organizations/" + fileName)
                    print("moved: " + fileName)
                elif arr[1] == "bookNote": 
                    moveFile(file, vaultPath + "/Books/" + fileName)
                    print("moved: " + fileName)
                else: 
                    print("subtype not processed yet - " + arr[1])
            # end if 
 


# Program Entry 
now = datetime.datetime.now()

print("Program Start: " + now.strftime("%Y-%m-%d %H:%M:%S"))


vaultPath = "/Users/nas/Library/Mobile Documents/iCloud~md~obsidian/Documents/NAS_remote_1"

inboxPath = vaultPath + "/Inbox"
# print(inboxPath)
 

# Go thru all the files in the inboxFolder
for root, dirs, files in os.walk(inboxPath):
    for fileName in files:
        filePath = inboxPath + "/" + fileName
        print(filePath)
        if "DS_Store" not in filePath: 
            readFile(filePath, fileName, vaultPath)  





now = datetime.datetime.now()

print("Program End: " + now.strftime("%Y-%m-%d %H:%M:%S"))
 