import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def root(n, r):
    base = n ** (1.0/r)
    roots = [base]
    for i in range(1, r):
        roots.append(complex(base * math.cos(2*math.pi * i / r), base * math.sin(2*math.pi * i / r)))
    return roots

def plot_dots_in_a_circle(N):
    roots = root(1, N)
    X = [ z.real for z in roots ]
    Y = [ z.imag for z in roots ]
    plt.scatter(X, Y, c=range(N), cmap="gist_rainbow")

    return tuple(((x, y) for x, y in zip(X, Y)))

def get_multiplication(n, N):
    if n >= N:
        return []
    out = []
    for a in range(N):
        out.append( (a, (a * n) % N) )
    return out

def get_addition(n, N):
    if n >= N:
        return []
    out = []
    for a in range(N):
        out.append( (a, (a + n) % N) )
    return out

def linear_interpolate(C1, C2, m):
    x1, y1 = C1
    x2, y2 = C2
    d = math.ceil(m) - math.floor(m)

    return x1 + d * (x2 - x1), y1 + d * (y2 - y1)

def connect_dots(n, N, coords):
    points = get_multiplication(n, N)
    #points = get_addition(n, N)            # not as interesting
    for (from_idx, to_idx) in points:
        if from_idx == to_idx:
            continue
        
        X = (0, 0)
        Y = (0, 0)
        from_coord = coords[from_idx]
        to_coord = linear_interpolate(coords[math.floor(to_idx) % N], coords[math.ceil(to_idx) % N], to_idx)
        X = (from_coord[0], to_coord[0])
        Y = (from_coord[1], to_coord[1])
        
        plt.plot(X, Y, color='white', zorder=0, alpha=0.1)

def make_plot(n, N):
    print(n)
    plt.clf()
    plt.style.use('dark_background')
    coords = plot_dots_in_a_circle(N)
    connect_dots(n, N, coords)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    #plt.show()

def make_gif(start, end, N, step=1):
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    anim = FuncAnimation(fig, lambda n: make_plot(n, N), frames=np.arange(start, end+step, step), interval=100)
    anim.save(f"modular_{N}_smooth.gif", dpi=400, writer='imagemagick')

if __name__ == "__main__":
    make_gif(2, 50, 200, step=0.1)