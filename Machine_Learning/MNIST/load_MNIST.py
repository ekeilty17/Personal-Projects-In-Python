import struct
import os
import gzip
from array import array
import numpy as np
import matplotlib.pyplot as plt

""" How this works, because the code is not very readable
1)  Gets path to ubyte file
2)  upzips the .gz file at that path. f_img/f_lbl are of type '_io.BufferedReader'
3)  The file that we opened is a ubyte file, so we need something to correctly interpret it
    This is what struct.unpack() does
        - f_img.read(16) reads the first 16 bits of the file. Likewise f_lbl.read(8) reads the first 8 bits
        - '>IIII' and '>II' tells struct.unpack how to unpack the data. So the 'IIII' means give a tuple with 4 items in it 
           and the '>' gives the byte order. '>' = big-endian, '<' = little-endian (google it)
        - The magic number (also called file signature) is a unique set of numbers at the beginning of a file indiciating its file type
        - N = number of samples
        - rows, cols = dimensions of image
4) 'B' = unsigned char, 'b' = signed char. It's just the datatypes of the files. f_img.read() reads the entire file
5) convert images to numpy array and reshape if necessary
"""

training_img_file = "train-images-idx3-ubyte.gz"
training_label_file = "train-labels-idx1-ubyte.gz"

def get_training_data(path="data"):
    
    fname_img = os.path.join(path, training_img_file)
    with gzip.open(fname_img, 'rb') as f_img:
        magic_num, N, rows, cols = struct.unpack(">IIII", f_img.read(16))
        img = array("B", f_img.read())
    images = np.array(img).reshape(N, rows, cols)

    fname_lbl = os.path.join(path, training_label_file)
    with gzip.open(fname_lbl, 'rb') as f_lbl:
        magic_num, N = struct.unpack(">II", f_lbl.read(8))
        lbl = array("b", f_lbl.read())
    labels = np.array(lbl)

    return images, labels


testing_img_file = "t10k-images-idx3-ubyte.gz"
testing_label_file = "t10k-labels-idx1-ubyte.gz"

def get_testing_data(path="data"):
    
    fname_img = os.path.join(path, testing_img_file)
    with gzip.open(fname_img, 'rb') as f_img:
        magic_nr, N, rows, cols = struct.unpack(">IIII", f_img.read(16))
        img = array("B", f_img.read())
    images = np.array(img).reshape(N, rows, cols)

    fname_lbl = os.path.join(path, testing_label_file)
    with gzip.open(fname_lbl, 'rb') as f_lbl:
        magic_nr, N = struct.unpack(">II", f_lbl.read(8))
        lbl = array("b", f_lbl.read())
    labels = np.array(lbl)

    return images, labels

def plot_image(image, label):
    plt.imshow(image, cmap=plt.cm.gray)
    plt.grid()
    plt.title(f"Label: {label}")
    plt.show()

if __name__ == "__main__":
    
    #images, labels = get_testing_data()
    images, labels = get_training_data()

    i = 1771
    plot_image(images[i], labels[i])