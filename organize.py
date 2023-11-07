import os # operations system
import shutil

from_dir = "C:/Users/lucas/Downloads/"
to_dir = "C:/Users/lucas/Documents/"

lista = os.listdir(from_dir)
print(lista)

for i in lista:
    name,extension = os.path.splitext(i)
    print(name)
    print(extension)

    if extension in [".pdf",".ini",".exe",".zip"]:
        path1 = from_dir + i
        path2 = to_dir + "downloads/"
        path3 = to_dir + "downloads/"+i


        if os.path.exists(path2):
            print("Movendo o aqrquivo",i)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Movendo o aqrquivo",i)
            shutil.move(path1,path3)














