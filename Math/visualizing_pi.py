import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.collections as mcoll
import matplotlib.path as mpath
from matplotlib.colors import ListedColormap, BoundaryNorm

with open("pi.txt") as f:
    pi = ''.join(f.read().split('\n'))

# get rid of decimal
pi = pi[:1] + pi[2:]

def root(n, r):
    base = n ** (1.0/r)
    roots = [base]
    for i in range(1, r):
        roots.append(complex(base * math.cos(2*math.pi * i / r), base * math.sin(2*math.pi * i / r)))
    return roots

def plot_dots_in_a_circle(N):
    roots = root(25, N)
    X = [ z.real for z in roots ]
    Y = [ z.imag for z in roots ]
    plt.scatter(X, Y, c=[ (i * 10) // N for i in range(N) ], cmap="gist_rainbow")

    return tuple(((x, y) for x, y in zip(X, Y)))

def get_segments(from_coord, to_coord, step=0.1):
    
    t = np.arange(0, 1+step, step)
    X = from_coord[0] + t * (to_coord[0] - from_coord[0])
    Y = from_coord[1] + t * (to_coord[1] - from_coord[1])

    points = np.array([X, Y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments

def colorline(from_coord, to_coord, from_color, to_color, z=None, alpha=1.0):
    """
    Plot a colored line with coordinates x and y
    Optionally specify colors in the array z
    Optionally specify a colormap, a norm function and a line width
    """

    segments = get_segments(from_coord, to_coord)

    # Default colors equally spaced on [0,1]:
    if z is None:
        z = np.linspace(0.0, 1.0, segments.shape[0])
    # Special case if a single number:
    if not hasattr(z, "__iter__"):  # to check for numerical input -- this is a hack
        z = np.array([z])
    z = np.asarray(z)

    cmap = ListedColormap([from_color, to_color])
    #norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
    norm = plt.Normalize(0.0, 1.0)

    lc = mcoll.LineCollection(segments, array=z, cmap=cmap, norm=norm, alpha=alpha)
    plt.gca().add_collection(lc)
    return lc

def to_index(d, count, N):
    return N * d // 10 + count

def make_plot(N):

    colors = ['red', 'orange', 'yellow', 'white', 'green', 'white', 'white', 'blue', 'purple', 'pink']

    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    coords = plot_dots_in_a_circle(N)
    counts = [0] * 10
    for i in range(N-1):
        d, nxt = int(pi[i]), int(pi[i+1])

        if d == nxt:
            continue
        
        from_coord = coords[to_index(d, counts[d], N)]
        to_coord = coords[to_index(nxt, counts[nxt], N)]
        colorline(from_coord, to_coord, colors[d], colors[nxt], None, alpha=0.05)
        counts[d] += 1

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    #plt.colorbar()
    plt.show()

if __name__ == "__main__":
    make_plot(1000)

    """
    N = 10
    np.random.seed(101)
    x = np.random.rand(N)
    y = np.random.rand(N)
    fig, ax = plt.subplots()

    path = mpath.Path(np.column_stack([x, y]))
    verts = path.interpolated(steps=3).vertices
    x, y = verts[:, 0], verts[:, 1]
    print(x)
    z = np.linspace(0, 1, len(x))
    colorline(x[-2:], y[-2:], z, cmap=plt.get_cmap('jet'))
    plt.show()
    """
    