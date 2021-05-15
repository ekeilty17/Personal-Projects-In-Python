def encrypt(s, key):
    out = ''
    for i in range(0,len(s),len(key)):
        for j in range(0,len(key)):
            if i+j < len(s):
                out += chr( ord(s[i+j]) ^ ord(key[j]) )
    return out

S = "Hello, how are you. I am coding in Pythong and stuff"

print "Original:"
print S
print

key = "wowww"
S_new = encrypt(S, key)
print "Encrypted:"
print S_new
print

S_back = encrypt(S_new, key)
print "Decrypted:"
print S_back
print
