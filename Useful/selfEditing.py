file_name = "selfEditing.py"

with open(file_name, 'r') as f:
    lines = f.readlines()
lines += 'print "This is added content"\n' 

with open(file_name, 'w') as g:
    g.writelines(lines)
