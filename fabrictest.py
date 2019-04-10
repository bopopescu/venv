#!/usr/bin/python
#from fabric import *

#result = Connection(host='127.0.0.1', user='root', port='32769', connect_kwargs={"key_filename": "/home/eblaghodir/.ssh/id_rsa.pub"})
#print(result.run('df'))
host = '127.0.0.1'
user = 'root'
port = 32769
key='/home/eblaghodir/.ssh/id_rsa'

import paramiko


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, port=port, key_filename=key)
result = stdin, stdout, stderr = client.exec_command('./test')
data = stdout.read() + stderr.read()

print(data)
client.close()
