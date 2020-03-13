import os
import sys
import calendar
import time
from functools import reduce

ts = calendar.timegm(time.gmtime())

def createPath(x, y):
    return os.path.join(x, y)


mypath = reduce(createPath, ['raw-images', 'persian-cat'])

cwd = os.getcwd()

list = ""

for index, fullFileName in enumerate(os.listdir(mypath), start=0):
    filename, file_extension = os.path.splitext(fullFileName)
    if filename and file_extension[1:] == 'jpg':
        print(filename)
        print(file_extension)
        origin = reduce(createPath, [cwd, mypath, filename+file_extension])
        new = reduce(createPath, [cwd, mypath, str(
            index) + '_'+str(ts) + file_extension])
        print(new)

        try:
            os.rename(origin, new)

            list = list + str(index) + '_'+str(ts) + file_extension + "\n"
            print('done')
        except:
            print("An exception occurred")

a = open('somefile.txt', 'w')
a.write(list)
a.close()
