#!/usr/bin/python3.6
import sys
import os
import shutil


if (len(sys.argv) < 4):
    print("not correct parameters")
    exit(1)

file_name = sys.argv[1]
limitsize = sys.argv[2]
logfilesize = sys.argv[3]

if(os.path.isfile(file_name) == True):
    logfilesize = os.stat(file_name).st_size
    logfilesize = logfilesize/1024

    if(logfilesize >= limitsize):
        for curentfilename in range(longsfile, 1, -1):
            src = file_name + "_" + curentfilename -1
            dst = file_name + "-" + curentfilename
            if (os.path.isfile(src) == True):
                shutil.copy(src,dst)
                print("copied " + src + " to " +dst)

        shutil.copy(file_name, file_name + "_1")
        print("copy " + file_name + " to " + file_name +"_1")
    myfile = open(file_name, 'w')
    myfile.close()

