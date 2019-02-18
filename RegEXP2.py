import  re
import json
filename = "D:/python/temp/dataFeb-16-2019.txt"
resultfile = "D:/python/temp/result.txt"

inputfile = open(filename, mode="r")
newfile = open(resultfile, mode="w")

lookfor = r"[\w.-]+@(?!nascetur\.ca)[\w]+.+[\w]+"
#text = inputfile.read()
#result  = re.findall(lookfor, text)
#for item in result:
#    print(item)
text = inputfile.read()
result  = re.findall(lookfor, text)
for item in result:
    print(item)
    newfile.write(item)

print("TOTAL=" +str(len(result)))


"""
for str in text:
    result  = re.findall(lookfor, str)
    print(result)
    if len(result) !=0:
        print(result)
#       newfile.write(str(result))


"""
"""
for str in newfile:
    print(str)
"""