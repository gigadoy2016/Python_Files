#create by Rangsan 22-Jan-2021
# 
# 
# last update 2021-01-22
import os
import sys

root = "D:/12_Preparation/calories/preparedata/data"
folderTrain = "obj"
folderTest = "test"
image_files = []
image_train = []
image_test = []

arguments = sys.argv #รับค่า root มาแทน Default

if(len(arguments)>1):
    root = arguments[1].replace('\\','/')
root = root + '/'
trainPath = root + folderTrain
testPath = root + folderTest


print(root)
os.chdir(root)

#print("1st +++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for folder in os.listdir(os.getcwd()):
    #print("-------------------------------------------------------------")
    print(folder)
'''    if os.path.isdir(folder): 
        os.chdir(os.path.join(os.getcwd(), folder))
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".jpg"):
                #print(folder+"/"+filename)
                image_files.append("test"+"/"+folder+"/" + filename)    
        os.chdir("..")
'''
os.chdir("..")
'''
with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\r\n")
    outfile.close()
os.chdir("..")
'''
def createFolder(name){
    path.exists(name)
}