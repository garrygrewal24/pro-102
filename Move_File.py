import os
import shutil

from_dir="C:/Users/DELL/Downloads"
to_dir="C:/Users/DELL/Downloads"

listFiles=os.listdir(from_dir)
#print(listFiles)

for fileName in listFiles:
    name, ext = os.path.splitext(fileName)
    #print(name)
    #print(ext)
    if ext=='':
        continue
    if ext in ['.txt','.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + fileName
        path2 =  to_dir + '/' + "Document_Files"
        path3 =  to_dir + '/' + "Document_Files" + '/' + fileName

    if os.path.exists(path2):
        print("moving" + fileName)  
        shutil.move(path1,path3) 

    else :
        os.makedirs(path2)
        print("moving" + fileName)  
        shutil.move(path1,path3)  