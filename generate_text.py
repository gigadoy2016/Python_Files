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
root = root
trainPath = root +"/"+ folderTrain
testPath = root +"/"+ folderTest

print(root)
#------------------------------------------------------------------
def folderGen(dPath):
    #print(dPath)    
    os.chdir(dPath)    
    for fileName in os.listdir(os.getcwd()):
        path = dPath +"/"+ fileName
        print(path)
        if os.path.isdir(path):
            #print(">>>>")
            folderGen(path)
        else:
            if fileName.endswith(".jpg"):
                image_files.append(path)                
        os.chdir("..")
#------------------------------------------------------------------
def writeTxt(fileName){
    with open(fileName, "w") as outfile:
        for image in image_files:
            outfile.write(image)
            outfile.write("\n")
        outfile.close()
    os.chdir("..")
}
#------------------------------------------------------------------
folderGen(trainPath)
writeTxt("train.txt")

folderGen(testPath)
writeTxt("test.txt")
#print(image_files)