import numpy as np
from activation_functions import activation_function, activation_derivative
from error import Error
from read_samples import *

class NeuralNetwork(object):

    def __init__(self, n_inputs, n_outputs, g_0='sigmoid', error='crossentropy', alpha=0.5, biases=True):
        self.dims = [n_inputs, n_outputs]
        self.G = ['identity', g_0]
        self.error = error
        self.alpha = alpha
        self.Z = []
        self.Weights = []
        self.isBiases = biases
        self.Biases = []

    def add_layer(self, n_nodes, g='relu'):
        self.dims = self.dims[:-1] + [n_nodes] + self.dims[-1:]
        self.G = self.G[:-1] + [g] + self.G[-1:]

    def compile(self):
        for i in range(len(self.dims)-1):
            self.Weights += [np.random.rand(self.dims[i], self.dims[i+1])]
            
            if self.isBiases is True:
                self.Biases += [np.random.rand(self.dims[i+1])]
            elif type(self.isBiases) is int or type(self.isBiases) is float:
                self.Biases += [np.full(self.dims[i+1], self.isBiases)]
            else:
                self.Biases += [np.zeros(self.dims[i+1])]

    def train(self, X_train, Y_train, epochs=50):
        for i in xrange(epochs):
            for x, y in zip(X_train, Y_train):
                # Feed forward through all layers
                self.feed_forward(x)
                self.back_propogate(y)

    def predict(self, x):
        self.feed_forward(x)
        return activation_function(self.Z[-1], self.G[-1])

    def feed_forward(self, x):
        #z = Wx + b
        self.Z = [np.array(x)]
        for W, b, g in zip(self.Weights, self.Biases, self.G[:-1]):
            # we need to transpose W because x is in row vector form
            self.Z += [ np.dot(W.T, activation_function(self.Z[-1], g)) + b ]
    
    def back_propogate(self, y):
        # W' = W - alpha * dE/dW
        
        y = np.array(y)
        y_hat = activation_function(self.Z[-1], self.G[-1])
        dW = []
        
        # Output Layer
        dE_dA = Error(y, y_hat, self.error)
        dA_dZ = activation_derivative(self.Z[-1], self.G[-1])
        dZ_dW = activation_function(self.Z[-2], self.G[-2])

        # Total Error
        dE_dW = np.transpose([dZ_dW]) * np.array([dE_dA * dA_dZ])
        #print dE_dW
        dW = [self.alpha * dE_dW] + dW

        Z_prev = self.Z[-2]
        g_prev = self.G[-2]
        for W, g, Z in reversed(zip(self.Weights[1:], self.G[:-2], self.Z[:-2])):
            
            # Propogating error back one layer
            dZ_dH = W
            dE_dH = dZ_dH * np.array([dE_dA * dA_dZ])
            dE_dA = np.array([ sum(row) for row in dE_dH ])

            # Total Error
            dA_dZ = activation_derivative(Z_prev, g_prev)
            dZ_dW = activation_function(Z, g)
            dE_dW = np.transpose([dZ_dW]) * np.array([dE_dA * dA_dZ])
            #print dE_dW
            dW = [-self.alpha * dE_dW] + dW

            Z_prev = Z
            g_prev = g

        self.Weights = [W + dw for W, dw in zip(self.Weights, dW)]
        

if __name__ == "__main__":
    

    # Setting up Neural Network
    N = NeuralNetwork(3, 2, "sigmoid", error="squared", alpha=0.01, biases=None)
    N.add_layer(2, "sigmoid")
    N.compile()

    # Manually creating weights
    #N.Weights = [ np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]), np.array([[0.7, 0.8], [0.9, 0.1]]) ]

    print "\nNodes after Feed Forward"
    x = [1, 4, 5]
    N.feed_forward(x)
    for layer in N.Z:
        print activation_function(layer, g='sigmoid')
    print

    print "\nPrediction"
    print N.predict(x)

    y = [0.1, 0.05]
    print "\nBack Propogation"
    for i in range(10000):
        N.back_propogate(y)

    print "\nPrediction"
    print N.predict(x)

    """
    # Setting up Neural Network
    N = NeuralNetwork(2, 1, "none", alpha=0.05, biases=False)
    N.add_layer(2, "none")
    N.compile()

    # Manually creating weights
    N.Weights = [ np.array([[0.11, 0.12], [0.21, 0.08]]), np.array([[0.14], [0.15]]) ]

    N.feed_forward([2, 3])
    for layer in N.Z:
        print layer

    y = [1]
    #N.back_propogate(y)
    """

    """
    # Setting up Neural Network
    N = NeuralNetwork(784, 10, "softmax")
    N.add_layer(3, "relu")
    N.add_layer(4, "sigmoid")
    N.compile()
    
    # Getting Training data
    X_train, Y_train = get_training_data()
    
    for x, y in zip(X_train[:2], Y_train[:2]):
        print x
        print y
        print

    N.train(X_train[:1], Y_train[:1], 1)
    
    print
    for W in N.Weights:
        print W
        print
    """

