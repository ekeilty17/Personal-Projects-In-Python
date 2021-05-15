import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import gamma

def N(a, b, u, sigma, plot=False):

    a = float(a)
    b = float(b)
    u = float(u)
    sigma = float(sigma)

    x = np.arange(u - 5*sigma, u + 5*sigma, 0.001 * sigma)
    n = 1.0/(np.sqrt(2 * np.pi) * sigma) * np.exp( - 1.0/(2*sigma**2) * (x - u)**2)
    
    L = "Mean = " + str(u) + ", StdDev = " + str(sigma)
    plt.plot(x, n, label=L)
    plt.fill_between(x, n, 0, where= (x>=a) & (x<=b), color='r')
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("Normal Distribution")
    
    def nn(x):
        return 1.0/(np.sqrt(2 * np.pi) * sigma) * np.exp( - 1.0/(2*sigma**2) * (x - u)**2)
    
    area = quad(nn, a, b)
    print area
    
    if plot:
        plt.legend(loc='upper right')
        plt.show()
    
    return area

def uniform(A, B, plot=True):
    
    A = float(A)
    B = float(B)

    x = np.arange(A - (B-A)/2.0, B + (B-A)/2.0, 0.01)
    f = np.piecewise(x, [x<A, x>B, ], [0, 0, 1.0/(B-A)])
     
    L = "A = " + str(A) + ", B = " + str(B) 
    plt.plot(x, f)
    plt.xlabel("x")
    plt.ylabel("1/(B - A)")
    plt.title("uniform distribution")
    if plot:
        plt.legend(loc='upper right')
        plt.show()

    return [(A+B)/2.0, (B-A)**2/12.0]

def Gamma(a, b, plot=True):
    
    a = float(a)
    b = float(b)

    x = np.arange(0, 10, 0.01)
    f = (1.0/(b**a * gamma(a))) * x**(a-1) * np.exp(-x / float(b))    
    
    L = "a = " + str(int(a)) + ", b = " + str(int(b)) 
    plt.plot(x, f, label=L)
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("gamma distribution")
    if plot:
        plt.legend(loc='upper right')
        plt.show()
    
    return [a*b, a*b**2]

def G(a, b, x1, x2, plot=True):
    a = float(a)
    b = float(b)

    x = np.arange(0, 20, 0.01)
    f = (1.0/(b**a * gamma(a))) * x**(a-1) * np.exp(-x / float(b))

    L = "a = " + str(int(a)) + ", b = " + str(int(b))
    plt.plot(x, f, label=L)
    plt.fill_between(x, f, 0, where= (x>=x1) & (x<=x2), color='r')
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("gamma distribution")
    
    def gg(x):
        return (1.0/(b**a * gamma(a))) * x**(a-1) * np.exp(-x / float(b))

    area = quad(gg, x1, x2)
    print area
    
    if plot:
        plt.legend(loc='upper right')
        plt.show()
    
    return area

def Exponential(b, plot=True):

    b = float(b)

    x = np.arange(0, 10, 0.01)
    f = (1.0/b) * np.exp(-x / float(b))

    L = "b = " + str(int(b))
    plt.plot(x, f, label=L)
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("exponential distribution")
    if plot:
        plt.legend(loc='upper right')
        plt.show()

    return [b, b**2]

def Chi_squared(v, plot=True):
    
    v = float(v)

    x = np.arange(0, 10, 0.01)
    f = (1.0/(2**(v/2.0) * gamma(v/2.0))) * x**(v/2.0 - 1) * np.exp(-x/2.0)

    L = "v = " + str(int(v))
    plt.plot(x, f, label=L)
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("chi-squared distribution")
    if plot:
        plt.legend(loc='upper right')
        plt.show()

    return [v, 2*v]

def X2(v, x1, x2, plot=True):
    
    v = float(v)

    x = np.arange(0, 50, 0.01)
    f = (1.0/(2**(v/2.0) * gamma(v/2.0))) * x**(v/2.0 - 1) * np.exp(-x/2.0)

    L = "v = " + str(int(v))
    plt.plot(x, f, label=L)
    plt.fill_between(x, f, 0, where= (x>=x1) & (x<=x2), color='r')
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("chi-squared distribution")
    
    def cc(x):
        return (1.0/(2**(v/2.0) * gamma(v/2.0))) * x**(v/2.0 - 1) * np.exp(-x/2.0)

    area = quad(cc, x1, x2)
    print area

    if plot:
        plt.legend(loc='upper right')
        plt.show()

    return area

def Weibull(a, b, plot=True):
    
    a = float(a)
    b = float(b)

    x = np.arange(0, 2, 0.01)
    f = a*b*x**(b-1)*np.exp(-a*x**b)

    L = "a = " + str(int(a)) + ", b = " + str(int(b))
    plt.plot(x, f, label=L)
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("Weibull distribution")
    if plot:
        plt.legend(loc='upper right')
        plt.show()
    
    return [a**(-1.0/b)*gamma(1 + 1.0/b), a**(-2.0/b) * (gamma(1 + 2.0/b) - gamma(1 + 1.0/b)**2)]

def W(a, b, x1, x2, plot=True):
    
    if x1 < 0 or x2 < 0:
        raise TypeError("Weibull function only defined for x > 0.")
    
    a = float(a)
    b = float(b)

    x = np.arange(0, 10, 0.01)
    f = a*b*x**(b-1)*np.exp(-a*x**b)

    L = "a = " + str(int(a)) + ", b = " + str(int(b))
    plt.fill_between(x, f, 0, where= (x>=x1) & (x<=x2), color='r')
    plt.plot(x, f, label=L)
    plt.xlabel("x")
    plt.ylabel("")
    plt.title("Weibull distribution")
    
    area = np.exp(-a*x1**b) - np.exp(-a*x2**b)
    print area
    
    if plot:
        plt.legend(loc='upper right')
        plt.show()

    return area

def t(v, plot=True):
    
    v = float(v)

    t = np.arange(-5, 5, 0.01)
    h = gamma((v+1)/2.0) / (gamma(v/2.0) * np.sqrt(np.pi * v)) * (1 + t**2/v)**(-(v+1)/2.0)

    L = "v = " + str(int(v))
    plt.plot(t, h, label=L)
    plt.xlabel("t")
    plt.ylabel("h(t)")
    plt.title("t-distribution")
    if plot:
        plt.legend(loc='upper right')
        plt.show()

def T(v, t1, t2, plot=True):
    
    v = float(v)

    t = np.arange(-5, 5, 0.01)
    h = gamma((v+1)/2.0) / (gamma(v/2.0) * np.sqrt(np.pi * v)) * (1 + t**2/v)**(-(v+1)/2.0)

    L = "v = " + str(int(v))
    plt.plot(t, h, label=L)
    plt.fill_between(t, h, 0, where= (t>=t1) & (t<=t2), color='r')
    plt.xlabel("t")
    plt.ylabel("h(t)")
    plt.title("t-distribution")
    
    def hh(t):
        return gamma((v+1)/2.0) / (gamma(v/2.0) * np.sqrt(np.pi * v)) * (1 + t**2/v)**(-(v+1)/2.0)

    area = quad(hh, t1, t2)
    print area
    
    if plot:
        plt.legend(loc='upper right')
        plt.show()

    return area

def f(v1, v2, plot=True):

    v1 = float(v1)
    v2 = float(v2)
    
    f = np.arange(0, 4, 0.01)
    
    coef = ( gamma((v1+v2)/2.0) * (v1/v2)**(v1/2.0) ) / ( gamma(v1/2.0) * gamma(v2/2.0) )
    h = coef * f**(v1/2.0 - 1) / ( (1 + v1*f/v2)**((v1+v2)/2) )

    L = "v1 = " + str(int(v1)) + ", v2 = " + str(int(v2))
    plt.plot(f, h, label=L)
    plt.xlabel("f")
    plt.ylabel("h(f)")
    plt.title("F-distribution")
    if plot:
        plt.legend(loc='upper right')
        plt.show()

def F(v1, v2, f1, f2, plot=True):

    v1 = float(v1)
    v2 = float(v2)
   
    f = np.arange(0, 4, 0.01)
   
    coef = ( gamma((v1+v2)/2.0) * (v1/v2)**(v1/2.0) ) / ( gamma(v1/2.0) * gamma(v2/2.0) )
    h = coef * f**(v1/2.0 - 1) / ( (1 + v1*f/v2)**((v1+v2)/2) )

    L = "v1 = " + str(int(v1)) + ", v2 = " + str(int(v2))
    plt.plot(f, h, label=L)
    plt.fill_between(f, h, 0, where= (f>=f1) & (f<=f2), color='r')
    plt.xlabel("f")
    plt.ylabel("h(f)")
    plt.title("F-distribution")
    
    def hh(f):
        return coef * f**(v1/2.0 - 1) / ( (1 + v1*f/v2)**((v1+v2)/2) )

    area = quad(hh, f1, f2)
    print area

    if plot:
        plt.legend(loc='upper right')
        plt.show()

    return area
  
X2(7, 1, 3)
