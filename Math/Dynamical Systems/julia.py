import numpy as np
import matplotlib.pyplot as plt

class Julia(object):

    def __init__(self, c, d=2):
        self.c = c
        self.d = d
    
    def plot(self, n_iterations=50, r=2.5, density=400, real_range=(-2.5, 1.5), imaginary_range=(-1.5, 1.5), save_as=None):
        # Making sure save_as is in the right format
        save_as = f"julia_{str(self.c).replace('.', '_')}.png" if save_as == None else save_as
        save_as = f"{save_as}.png" if save_as[-4] != '.' else save_as

        # Real axis
        x1, x2 = real_range
        x = np.linspace(x1, x2, 4 * density + 1)
        
        # Imaginary Axis
        y1, y2 = imaginary_range
        y = np.linspace(y1, y2, 3 * density + 1)
        
        # Creating mesh of complex numbers acting as the starting point
        A, B = np.meshgrid(x, y)
        Z = A + B * 1j

        # "escape time" of each complex value in Z
        T = np.zeros(Z.shape)

        # Repeated iterations
        for k in range(n_iterations):
            print(k)

            # Matrix of True, False. True meaning have not converged yet
            M = abs(Z) < r

            # applying iteration to only indices of M that valuation to True
            Z[M] = Z[M] ** self.d + self.c

            # For indices of M that are still True, we increment by 1
            T[M] += 1

        #plt.xticks(np.arange(0, 4 * density, 500), np.arange(-2.5, 1.5, 0.5))
        #plt.yticks(np.arange(0, 3 * density, 500), np.arange(-1.5, 1.5, 0.5))
        plt.imshow(T, cmap=plt.cm.twilight_shifted)
        plt.savefig(f"media/{save_as}", dpi=4*density)

if __name__ == "__main__":
    phi = (1 + 5 ** 0.5) / 2
    c = (phi - 2) + (phi - 1) * 1j
    J = Julia(c=1)
    J.plot(density=1000)