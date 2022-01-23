from hashlib import new
import os
import shutil

fromDir = "fromTest"

startYear = 2009
endYear = 2018

toDir = "3-12"

files = os.listdir(fromDir)

# Create new destinationFolder if it does not exist
try: 
    os.mkdir(toDir)
except:
    print("Folder already exists")

# For each year in the range (ending on the actual endYear)
# move each matching file fromDir toDir
for year in range(startYear, endYear+1):
    for file in files:
        if "_" + str(year) in file:
            fromPath = fromDir + "\\" + file
            toPath = toDir + "\\" + file
            shutil.move(fromPath, toPath)
            print(file)
