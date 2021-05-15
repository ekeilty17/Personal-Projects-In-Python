# I'm going to write a python script that creates a shell script that creates and executes a python script that prints "Hello, world"

import os

file_name = "hello_world.sh"
with open(file_name, 'w+') as g:
    g.write("python -c \"print 'Hello, World!'\"")

os.system("chmod 777 " + file_name)
os.system("./" + file_name)
