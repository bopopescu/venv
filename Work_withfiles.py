inputfile = 'D:/python/temp/pwgen.txt'
outputfile = 'D:/python/temp/newfile.txt'

pass_tofind = "vasya"

myfile1 = open(inputfile, mode='r', encoding='utf_8')
myfile2 = open(outputfile, mode='a', encoding='utf_8')
#print(myfile.read())
count = 0
for num, line in enumerate(myfile1,1):
    if (pass_tofind in line):
        print("Line" +str(num)+" " + line.strip())
        myfile2.write(line)
        count = count+1

        #myfile2.writable("forun" +line)
print (count)

myfile2.close()
myfile1.close()