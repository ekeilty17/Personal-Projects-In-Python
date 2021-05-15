def isVector(v):
    #checking that v is actually a list
    try:
        v[0]
    except:
        return False
    
    #checking that v is a single dimension array
    #checking that the elements of v are not strings
    for i in range(0,len(v)):
        if (type(v[i]) == list):
            return False
        if (type(v[i]) == str):
            return False

    return True


def magnitude(v):
    if (not(isVector(v))):
        return False

    import math
    sum = 0
    for e in v:
        sum += e*e

    return math.sqrt(sum)


def scalar(k,v):
    if (not(isVector(v))):
        return False
    
    for i in range(0,len(v)):
        v[i] = k*v[i]

    return v


def norm(v):
    if (not(isVector(v))):
        return False
    
    return scalar(1/magnitude(v),v)


def dot(v,w):
    #Checking that v and w are vectors
    if (not(isVector(v)) or not(isVector(w))):
        return False
    #making sure they are the same dimensions
    if len(v) != len(w):
        return False
    
    accum = 0
    for i in range(0,len(v)):
        accum += v[i]*w[i]
    return accum


def cross(v,w):
    #Checking that v and w are vectors
    if (not(isVector(v)) or not(isVector(w))):
        return False
    #making sure they are the same dimensions
    if ((len(v) != 3) or (len(w) != 3)):
        return False
    
    return [(v[1]*w[2]-v[2]*w[1]), (v[2]*w[0]-v[0]*w[2]), (v[0]*w[1]-v[1]*w[0])]


def angle(w,v):
    if (not(isVector(v)) or not(isVector(w))):
        return False
    
    import math
    return math.acos( dot(v,w) / (magnitude(v) * magnitude(w)) )


def proj(v,u):
    if (not(isVector(v)) or not(isVector(w))):
        return False
    
    return ( dot(v,u) / dot(v,v) )*v


def add(v,w):
    if (not(isVector(v)) or not(isVector(w))):
        return False
    if len(v) != len(w):
        return False
    for i in range(0,len(v)):
        v[i] += w[i]
    return v


def subtract(v,w):
    if (not(isVector(v)) or not(isVector(w))):
        return False
    if len(v) != len(w):
        return False
    for i in range(0,len(v)):
        v[i] -= w[i]
    return v
