import numpy as np
import matplotlib.pyplot as plt

def a_n(n):
    return 0

def b_n(n):
    if n%2 == 0:
        return 0
    return (4/np.pi) * (1 / (n))

def FS(L, N):
    interval = np.linspace(-1, 1, 500)

    total = np.zeros_like(interval)
    for n in range(N+1):
        total += a_n(n) * np.cos((2*np.pi*n)/L * interval) + b_n(n) * np.sin((2*np.pi*n)/L * interval)
    return interval, total

if __name__ == "__main__":
    x, y = FS(1, 100)
    plt.axvline(0, color='k')
    plt.axhline(0, color='k')
    plt.grid()
    plt.plot(x, y)
    plt.show()
