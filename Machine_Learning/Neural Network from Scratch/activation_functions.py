import numpy as np

def Sigmoid(X):
    return 1.0 / (1 + np.exp(-X)) 
def dSigmoid(X):
    return Sigmoid(X) * (1 - Sigmoid(X))

def ReLU(X):
    max_element = np.vectorize(lambda x: max(0, x))
    return max_element(X)
def dReLU(X):
    #max_element = np.vectorize(lambda x: max(0, x)/x)
    max_element = np.vectorize(lambda x: 1 if x>0 else 0)
    return max_element(X)

def Parametric_ReLU(X, a):
    pass
def dParametric_ReLU(X, a):
    pass

def Leaky_ReLU(X):
    return Parametric_ReLU(X, 0.01)
def dLeaky_ReLU(X):
    return dParametric_ReLU(X, 0.01)

def ELU(X, a):
    pass
def dELU(X, a):
    pass

def SELU(X):
    pass
def dSELU(X):
    pass

def CReLU(X):
    pass
def dCReLU(X):
    pass

def ReLU_6(X):
    pass
def dReLU_6(X):
    pass

def Softmax(X):
    return X / float(sum(X))
    #return np.exp(X) / float(sum(np.exp(X)))
def dSoftmax(X):
    
    def softmax(X):
        return np.exp(X) / float(sum(np.exp(X)))
    
    return softmax(X) * (1 - softmax(X))

def Identity(X):
    return X
def dIdentity(X):
    return np.ones(X.shape)

def activation_function(X, g='relu'):
    return {
                'sigmoid': Sigmoid,
                'relu': ReLU,
                'parametric_relu': Parametric_ReLU,
                'leaky_relu': Leaky_ReLU,
                'elu': ELU,
                'selu': SELU,
                'crelu': CReLU,
                'relu6': ReLU_6,
                'softmax': Softmax,
                'identity': Identity,
                'none': Identity
            }[g.lower()](X)

def activation_derivative(X, g='relu'):
    return {    
                'sigmoid': dSigmoid,
                'relu': dReLU,
                'parametric_relu': dParametric_ReLU,
                'leaky_relu': dLeaky_ReLU,
                'elu': dELU,
                'selu': dSELU,
                'crelu': dCReLU,
                'relu6': dReLU_6,
                'softmax': dSoftmax,
                'identity': dIdentity,
                'none': dIdentity
            }[g.lower()](X)

if __name__ == "__main__":
    #M = np.random.randint(-5, 5, size=(2, 4))
    #print M
    X = np.array([1.35, 1.27, -1.8])
    print X
    print dReLU(X)
