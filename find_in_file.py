import os, re, time

def replace_in_dir(workdir, key1, key2):
       directory = os.listdir(workdir)
       os.chdir(workdir)
       for file in directory:

             time1 = os.stat(file)
             (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
             print("last modified: %s" % time.ctime(mtime))
             open_file = open(file,'r')
             read_file = open_file.read()
             stat = os.stat(file)
             #print(stat)
#             print(read_file)
             regex = re.compile(key1)
#             print (regex)
 #            if(re.compile(key1)):
  #               print ("find neded text in" +file)
             read_file = regex.sub(key2, read_file)



#             if (os.)
#             print (read_file)
             write_file = open(file,'w')
             write_file.write(read_file)
             #print("file name is:" + file)
             time2 = os.path.getmtime(workdir)
             print(time2)
            # print(stat1.st_size)
             print("----------------------")

replace_in_dir('/home/eblaghodir/testdir/', 'aaa', 'bbb')
