import sys

ARG1=""
AGR2=""
ARG3=""
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
    if not skip:
        arg=sys.argv[i]
        print "INFO: processing",arg
        if arg == "--arg1":
            if i != nargs-1:
                ARG1=sys.argv[i+1]
                skip=True
        elif arg == "--arg2":
            if i != nargs-1:
                ARG2=sys.argv[i+1]
                skip=True
        elif arg == "--arg3":
            if i != nargs-1:
                ARG3=sys.argv[i+1]
                skip=True
        else:
            print "ERR: unknown arg:",arg
    else:
        skip=False

print "ARG1: ",ARG1
print "ARG2: ",ARG2
print "ARG3: ",ARG3
