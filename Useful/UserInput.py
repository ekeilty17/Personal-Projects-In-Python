""" Getting various user inputs with the correct error checking """

# Any String
print
inp = None
inp = raw_input("Please input any string: ")
print "Success!"


# A string that does not contain numbers
print
inp = None
valid = False
while not valid:
    inp = raw_input("Please input any string that does not contain numbers: ")
    valid = True
    for char in inp:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print "Invalid Input: Input contained a number."
            print
            valid = False
            break
print "Success!"

# A string that only contains english letters 
print
inp = None
valid = False
while not valid:
    inp = raw_input("Please input any word (not special characters): ")
    valid = True
    for char in inp:
        if char not in ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 
                        'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r',
                        'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']:
            print "Invalid Input: Input contained either numbers or special characters."
            print
            valid = False
            break
print "Success!"



# Any float
print
inp = None
valid = False
while not valid:
    try:
        inp = float(raw_input("Please input any number: "))
        valid = True
    except:
        print "Invalid Input: Input is not a number. Try again."
        print
print "Success!"

# Float in a range
print
inp = None
valid = False
while not valid:
    try:
        inp = float(raw_input("Please input any number between 1 and 10 (inclusive): "))
        if inp < 1 or inp > 10:
            print "Invalid Input: Input is out of range. Try again."
            print
        else:
            valid = True
    except:
        print "Invalid Input: Input is not a number. Try again."
        print
print "Success!"



# Any integer
print
inp = None
valid = False
while not valid:
    try:
        inp = float(raw_input("Please input any integer: "))
        if int(inp) != inp:
            print "Invalid Input: Input is a decimal, not an integer. Try again."
            print
        else:
            valid = True
    except:
        print "Invalid Input: Input is not a number. Try again."
        print
print "Success!"
inp = int(inp)


# Integer in a range
print
inp = None
valid = False
while not valid:
    try:
        inp = float(raw_input("Please input any integer between 1 and 10 (inclusive): "))
        if int(inp) != inp:
            print "Invalid Input: Input is a decimal, not an integer. Try again."
            print
        elif int(inp) < 1 or int(inp) > 10:
            print "Invalid Input: Input is out of range. Try again."
            print
        else:
            valid = True
    except:
        print "Invalid Input: Input is not a number. Try again."
        print
print "Success!"
inp = int(inp)


