file_name="datain"


# This is how most people open text files, but you really should do it this way
"""
try:
   f=open(file_name,'r')
except:
   print "ERR: file",file_name,"is not present or can't be opened"

lines = f.readlines()

f.close()
"""

# It's better to use a context manager to manage the resources for us
with open(file_name, 'r') as f:
    lines = f.readlines()

for line in lines:
   print line.split('\n')[0]

