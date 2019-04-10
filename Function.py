'''def sayhello(name):
    print("hello world" +name)
    print("whish yoo all the best")
    print("don't worry the best is yet to come")

def saybyby():
    print("thats all folks")

name = input()
sayhello(name)
saybyby()

'''

def summa(x,y):
    print(x+y)

#summa(10,23)

x = summa(23,10)

def fakt(x):
    "Faktorial"
    fak =1
    for i in range(1,x+1):
        fak = fak*i
    return fak


for i in range(1,100):
    print(str(i)+"!=\t"+str(fakt(i)))