import numpy as np
import matplotlib.pyplot as plt

class GeneralizedMandelbrotSet(object):

    def __init__(self, d=2):
        self.d = d
    
    def plot(self, n_iterations=100, r=2.5, density=400, real_range=(-2.5, 1.5), imaginary_range=(-1.5, 1.5), save_as=None):
        
        # Making sure save_as is in the right format
        save_as = f"mandelbrot_{str(self.d).replace('.', '_')}.png" if save_as == None else save_as
        save_as = f"{save_as}.png" if save_as[-4] != '.' else save_as

        # Real axis
        x1, x2 = real_range
        x = np.linspace(x1, x2, 4 * density + 1)
        
        # Imaginary Axis
        y1, y2 = imaginary_range
        y = np.linspace(y1, y2, 3 * density + 1)
        
        # Creating mesh of complex numbers acting as the + c
        A, B = np.meshgrid(x, y)
        C = A + B * 1j

        # starting point is 0 for all C
        Z = np.zeros_like(C)

        # "escape time" of each complex value in Z
        T = np.zeros(C.shape)

        # Repeated iterations
        for k in range(n_iterations):
            # Matrix of True, False. True meaning have not converged yet
            M = abs(Z) < r

            # applying iteration to only indices of M that valuation to True
            Z[M] = Z[M] ** self.d + C[M]

            # For indices of M that are still True, we increment by 1
            T[M] += 1

        #plt.xticks(np.arange(0, 4 * density, 500), np.arange(-2.5, 1.5, 0.5))
        #plt.yticks(np.arange(0, 3 * density, 500), np.arange(-1.5, 1.5, 0.5))
        plt.imshow(T, cmap=plt.cm.twilight_shifted)
        plt.savefig(f"media/{save_as}", dpi=4*density)

if __name__ == "__main__":
    M = GeneralizedMandelbrotSet(d=2)
    M.plot(n_iterations=50, density=1000)
    #M.plot(n_iterations=100, density=1000, real_range=(0.24, 0.26), imaginary_range=(-0.1, 0.1), r=1, save_as="zoom.png")