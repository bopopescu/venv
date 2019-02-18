#name = input("Please enter name: ")
#print("Privet " + name)
#num1 = input("Enter X: ")
#num2 = input("Ente Y: ")
#summa = int(num1) + int(num2)
#print(summa)
'''
message = ""
while True:
    message = input("Enter PASS ")
    print(message)
    if message == 'sekret':
        break
    print('PASS NOT CORRECT')

print("Pass was "  + message)
'''
mylist = []
msg = ""
while msg != 'stop':
    msg = input("Enter new item, and stop to finish ")
    mylist.append(msg)

print(mylist)