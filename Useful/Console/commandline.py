import os

# Run any shell command
os.system("ls")
print

# Getting path of file
file_name = "commandline.py"
print os.path.join( os.path.dirname(__file__), file_name )

# infinite loops
#os.system("python commandline.py")

# Current Working Directory
print os.getcwd()

# current process's user ID
print os.getuid()

# current operating system
print os.uname()

# Change the root directory of current process to specified path
#print os.chroot('.')

# Listall entities in specified path directory
print os.listdir('.')

# Manipulating individual files
with open("temp.txt", 'w+') as g:
    g.write("x = 10\n")
    g.write("print x\n")
os.rename("temp.txt", "temp.py")
os.remove("temp.py")

# Manipulating directories
os.mkdir("test1")
os.rmdir("test1")

# Manipulating directivies recursively
os.makedirs("test/test/test")
os.removedirs("test/test/test")
