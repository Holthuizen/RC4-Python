'''
    ARC4 or ARCFOUR Algorithm Class with stream generator. 
    Author: C.d.B.
    License: MIT
'''

class RC4: 
    def __init__(self,key):        
       #returns generator that can generate one word of the keystream at a time without a given limit
       self.keygenerator =  self.PRGA_YIELD( self.KSA(list(key.encode())))

    def KSA(self,key):
        s = list(range(0,256))#internal state, array [0 - 255] 
        j = 0
        for i in range(256):
            j = (j+s[i]+key[i%len(key)])% 256
            s[i],s[j] = s[j],s[i] #list swap
        return s
    
    def PRGA_YIELD(self,S):
        i,j = 0,0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # swap
            K = S[(S[i] + S[j]) % 256]
            yield K


# Test vectors  https://en.wikipedia.org/wiki/RC4 :
	
streamcipher = RC4("Key")
#Keystream = EB9F7781B734CA72A719… 	

# streamcipher = RC4("Wiki")	
#Keystream = 6044DB6D41B7 	

# streamcipher = RC4("Secret")
# Keystream = 04D46B053CA87B59 	

#get keystream generator
keystream = streamcipher.keygenerator
#format integers to hex
for c in range(10):
    print("%02X" % (next(keystream)),end='')


