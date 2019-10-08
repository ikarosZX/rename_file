import os

path = 'path/to/files'
fileList=os.listdir(path)

for i in fileList:
    oldname = path + i
    newname = path + 'newname'
    os.rename(oldname,newname) 
    
    print(oldname,'======>',newname)
    print('newname',newname)
