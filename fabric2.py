#!/usr/bin/python
from fabric import *

result = Connection(host='127.0.0.1', user='root', port='32769', connect_kwargs={"key_filename": "/home/eblaghodir/.ssh/id_rsa"})
print(result.run('df -h', hide=True))
print(result.run('./test', hide=True))