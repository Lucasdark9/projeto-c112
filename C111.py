import os
import shutil

path = "C:/Users/lucas/Downloads"

print(os.listdir(path))

source = path + "/Dog-walk.gif"
destination = path + "/copy_Dog-walk.gif"

shutil.copy(source,destination)

copys = path + "/copias"
#os.makedirs(copys)

futureCopy = path + "/copias/copy_Dog-walk.gif"


shutil.move(destination,futureCopy)










