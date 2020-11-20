'''
    ARC4 or ARCFOUR Algorithm Class with stream generator. 
    Author: C.d.B.
    License: MIT 
    git https://github.com/Holthuizen/RC4-Python 
'''

class RC4: 
    def __init__(self,key):  
        '''unit tests'''  
        if key == "":
            raise ValueError("key can not be empyt")
        if not isinstance(key, str):
            raise TypeError("key must be of type String")  

        #generator
        self.keygenerator =  self.PRGA_YIELD( self.KSA(list(key.encode())))

    #returns state array S
    def KSA(self,key):
        s = list(range(0,256))#internal state, array [0 - 255] 
        j = 0
        for i in range(256):
            j = (j+s[i]+key[i%len(key)])% 256
            s[i],s[j] = s[j],s[i] #list swap
        return s
    #returns keystream generator K
    def PRGA_YIELD(self,S):
        i,j = 0,0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # swap
            K = S[(S[i] + S[j]) % 256]
            yield K


# Test vectors  https://en.wikipedia.org/wiki/RC4 :

#example: 
keygenerator = RC4("Key").keygenerator
for c in range(10):
    print(next(keygenerator),end=' ') #bytes decimal, format to hex for comparison with test vectors. 

