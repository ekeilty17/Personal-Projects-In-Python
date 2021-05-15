import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 1/2.0

ax = plt.figure()
plt.bar(x, y, width, color="blue")

#plt.xticks(y_pos, x_pos)
#plt.ylabel('Usage')
plt.title('Sorting')

ax.savefig('frame'+str(0).zfill(5)+'.png',dpi=300)
ax.clear()
