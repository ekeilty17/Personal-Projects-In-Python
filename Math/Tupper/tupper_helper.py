from characters import *
from PIL import Image
import numpy as np

# This sort of works, but not well
def image_to_tupper(filename, H, W):

    img_size = (W, H)

    img = Image.open(filename)
    img = img.resize(img_size)
    img = img.convert(mode='1')

    K = 0
    # bit order uses cartesian coords, so count backward
    for x in reversed(range(0, img_size[0])):
        for y in range(0, img_size[1]):
            val = img.getpixel((x, y)) & 1
            K = (K << 1) | (1 ^ val)

    # multiply final result by H
    return K * H

def array_to_tupper(bmp):
    H = len(bmp)
    W = len(bmp[0])

    K = 0
    for x in reversed(range(W)):
        for y in range(H):
            val = bmp[y][x]
            K = (K << 1) |  val

    return K * H

def tupper_to_array(K, H, W):
    K /= H
    bmp = []
    for i in range(H):
        bmp += [[]]
    for x in range(W):
        for y in range(H):
            bmp[y] += [int(K & 1)]
            K = K >> 1
    return reversed(bmp)

def string_to_tupper(S):
    # dimensions of characters being used
    h = 9
    w = 7

    T = [list(tupper_to_array(char_to_tupper_9_7[s], h, w)) for s in S]
    bmp = []
    for i in range(9):
        bmp += [[]]

    for t in T:
        for i in range(9):
            bmp[i] += t[i]
            bmp[i] += [0]

    return array_to_tupper(bmp)
