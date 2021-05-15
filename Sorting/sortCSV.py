import sys

FIN=""
FOUT=""
COL=""
DIR=""
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
    if not skip:
        arg=sys.argv[i]
        #print "INFO: processing",arg
        if arg == "--fin":
            if i != nargs-1:
                FIN=sys.argv[i+1]
                skip=True
        elif arg == "--fout":
            if i != nargs-1:
                FOUT=sys.argv[i+1]
                skip=True
        elif arg == "--col":
            if i != nargs-1:
                COL=sys.argv[i+1]
                skip=True
        elif arg == "--dir":
            if i != nargs-1:
                DIR=sys.argv[i+1]
                skip=True
        else:
            print "ERR: unknown arg:",arg
    else:
        skip=False

#print "INFO: FIN",FIN
#print "INFO: FOUT",FOUT
#print "INFO: COL",COL
#print "INFO: DIR",DIR

run = True

if (DIR != '+' and DIR != '-'):
    print "ERR: input --dir needs to be + or -"
    run = False


f = open(FIN,'r')
lines=f.readlines()
f.close()
accum=[]
for i in lines:
    j=i.split('\n')[0]
    k=j.split(',')
    r=[]
    for x in k:
        r = r + [int(x)]
    accum = accum + [r]

for i in accum:
    try:
        int(COL)
        if (0 > int(COL) or len(i)-1 < int(COL)):
            print "ERR: --col is out of range of --fin"
            run = False
            break
        if (int(COL) != float(COL)):
            print "ERRL --col needs to be an integer"
            run = False
            break
    except:
        print "ERR: --col is not an integer"
        run = False
        break

if run:

    def sortKey(x):
        if DIR=='+':
            return x[int(COL)]
        elif DIR=='-':
            return -x[int(COL)]

    sorted_list = sorted(accum,key=sortKey)

    g = open(FOUT,'w')
    for i in sorted_list:
        for j in i:
            g.write(str(float(j)))
            if (j != i[len(i)-1]):
                g.write(',')
        g.write('\n')
    g.close()
