import os
import sys
import calendar
import time
ts = calendar.timegm(time.gmtime())


mypath = 'raw-images\persian-cat'

cwd = os.getcwd()
print(ts)

list = ""
for index, fullFileName in enumerate(os.listdir(mypath), start=0):
    filename, file_extension = os.path.splitext(fullFileName)
    if filename and file_extension[1:] == 'jpg':
        a = cwd + "\\" + mypath + "\\" + filename + file_extension
        b = cwd + "\\" + mypath + "\\" + \
            str(index) + '_'+str(ts) + file_extension

        try:
            os.rename(a, b)
            list = list + str(index) + '_'+str(ts) + file_extension + "\n"
            print('done')
        except:
            print("An exception occurred")

print(list)
