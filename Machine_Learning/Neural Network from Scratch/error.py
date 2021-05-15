def SquaredError(y, y_hat):
    #E = sum( 0.5 * (y - y_hat)**2 )
    return -(y - y_hat)

def CrossEntropy(y, y_hat):
    #E = - sum( y*np.log(y_hat) + (1-y)*np.log(1-y_hat) ) / len(y)
    return  - y/y_hat + (1-y)/(1-y_hat)

def Error(y, y_hat, error='crossentropy'):
    return  {
                'squared' : SquaredError,
                'squarederror' : SquaredError,
                'crossentropy' : CrossEntropy
            }[error](y, y_hat)
