import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def makeFrame(inp):
    
    #getting counter
    lines = open('temp.txt', 'r').readlines()
    i = lines[0]
    if lines[0] == "temp\n" or lines[0] == "temp":
        lines[0] = str(1)
        i = 0
    else:
        lines[0] = str(int(i) + 1)
    out = open('temp.txt', 'w')
    out.writelines(lines)
    out.close()

    N = len(inp)
    x = range(N)
    width = 1/2.0

    ax = plt.figure()
    plt.bar(x, inp, width, color="blue")

    plt.title('Merge Sort')

    ax.savefig('frame'+str(i).zfill(5)+'.png',dpi=300)
    ax.clear()
