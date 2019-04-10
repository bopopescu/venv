import sys

#inputfile = 'D:/python/temp/somefile.txt'
inputfile = 'MOD12file.py'

#myfile1 = open(inputfile, mode='r', encoding='utf_8')
#print(myfile1.read())
while True:
    try:
        print("inside try")
        myfile1 = open(inputfile, mode='r', encoding='utf_8')
    except Exception:
        print("inside except")
        print("error find")
        print(sys.exc_info()[1])
#    sys.exit()
        inputfile = input("enter filename:")
    else:
        print("inside else")
        print(myfile1.read())
        sys.exit()
    finally:
        print("inside finaly")

print("====================EOF===================")

