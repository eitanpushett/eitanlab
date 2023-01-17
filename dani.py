import os
path = "my-treerd-folder"
print(os.environ['CNVRG_JOB_ID'])
os.mkdir(path)
for i in range (1, 10000):
    f = open("{}/demofile{}.txt".format(path, i), "a")
    f.write("Now the file has more content!")
    f.close()
