import numpy as np

W1 = np.array([ [0.1, 0.4, 0.3],
                [0.3, 0.2, 0.7],
                [0.4, 0.3, 0.9]])

x = np.array([-3.70644, -1.4755, -1.6886])
b = np.array([0.15911, 0.2040, 0.3685])

x = [0.26979245, 0.32227714, 0.40793041]
y = [1.86706797, 2.23028232, 2.8204]

#for a, b, c, d in reversed(zip(x, y, x, y)):
#    print a, b, c, d

#print np.exp(x[2]) * (np.exp(x[0]) + np.exp(x[1])) / ( (np.exp(x[0]) + np.exp(x[1]) + np.exp(x[2]))**2 )


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 2, 2, 2]

print np.array([x]) * np.transpose([y])
