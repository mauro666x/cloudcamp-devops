import random
import os
import datetime

# Pick a random number to folder
randomFolder="./"+str(random.randint(1, 10))

# If folder exists, delete
try:
    for root, dirs, files in os.walk(randomFolder, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
    os.rmdir(randomFolder)
except FileNotFoundError as e:
    None

# Create the folder
os.mkdir(randomFolder)

# Create ten files
for i in range(0, 10):
    newFile=randomFolder+"/"+str(i)+".txt" 
    print("New file in : "+newFile)
    f = open(newFile, "w")
    f.write(str(datetime.datetime.now()))
    f.close()