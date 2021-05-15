file_name="dataout.txt"
#If you want to make sure the file is already present

#The + means if the file does not exist, then python will create it

with open(file_name, 'w+') as g:
    g.write("This is content\n")
    g.write("This is more content\n")


#function that replaces a line in a textfile
def replace_line(file_name, line_num, text):
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    print lines[line_num] #line being replaced
    lines[line_num] = text
    with open(file_name, 'w') as g:
        g.writelines(lines)
