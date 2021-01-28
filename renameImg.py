#create by Rangsan 25-Dec-2020
#update by Rangsan 28-Jan-2021
# Remane file with new name and add order numbers.
# arguments is new prefix name to display
# last update 2020-12-25
# sample   C:/python renameImg.py D:\12_Preparation\calories\scrapping\dataset\ไข่เจียวกุ้ง newname
import os
import sys
import shutil

arguments = sys.argv
#image_files = []

index = 0
#print(arguments[1])
#print(arguments[2])
os.chdir(arguments[1]+"\\")

for filename in os.listdir(os.getcwd()):
    #print(filename)
    #newName = +"ALL\\"+arguments[1]+filename
    if filename.endswith(".jpg"):
        newName = arguments[2]+'_'+str(index)+".jpg"
    if filename.endswith(".png"):
        newName = arguments[2]+'_'+str(index)+".png"
    #if filename.endswith(".txt"):
    #    newName = arguments[1]+'_'+str(index)+".txt"
    print(newName)
    shutil.copy2(filename, newName)
    os.remove(filename)
    index +=1
os.chdir("..")
