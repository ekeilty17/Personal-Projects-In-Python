import numpy as np
from mnist import MNIST

mndata = MNIST('samples')

def get_training_data():
    images, labels = mndata.load_training()
    labels = labels_to_vector(labels)
    return (images, labels)

def get_testing_data():
    images, labels = mndata.load_testing()
    labels = labels_to_vector(labels)
    return (images, labels)

def labels_to_vector(labels):
    out = []
    for i in range(len(labels)):
        out += [np.zeros((10))]
        out[-1][labels[i]] = 1
    return out


if __name__ == "__main__":
    import random
    
    images, labels = training_data()
    labels = labels_to_vector(labels)

    index = random.randrange(0, len(images))  # choose an index ;-)
    #print(mndata.display(images[index]))
    print
    print images[index]
    print
    print labels[index]
    print type(images)
