def repeated_squares(a, b, mod):
    a_2n = a % mod    #a^2n
    accum = 1

    while b != 0:
        #getting binary digit in the nth place of b
        last = b & 0b1
        b = b >> 1
        #if the binary digit in the nth palce of b is a 1, we multiply by a^2n
        if last == 1:
            accum *= a_2n
            #accum = accum % mod        #I'm not sure if this step would make it more or less efficient
        a_2n = (a_2n**2) % mod

    return accum % mod



print(repeated_squares(271, 321, 481))
print((271**321)%481)
