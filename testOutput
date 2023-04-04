import os
os.chdir("output")
path= os.getcwd()
for  i in range(5):    
    for j in range(5):
        os.mkdir("folder"+str(i)+str(j))
        os.chdir("folder"+str(i)+str(j))
        os.system('fallocate -l 0.1k '+"file"+str(i)+str(j))
    os.chdir(path)
for  i in range(5):
    os.system('fallocate -l 0.1k '+"file"+str(i))
os.chdir("/cnvrg")
