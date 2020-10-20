class RC4: 
    def __init__(self,key): 
       self.key =  self.PRGA( self.KSA( list(key.encode() ) ))#return generator that constantly updates the secret internal state S
    def KSA(self,key):
        s = list(range(0,256))#internal state (array from 0 to 255 )
        j = 0
        for i in range(256):
            j = (j+s[i]+key[i%len(key)])% 256
            s[i],s[j] = s[j],s[i] #list swap
        return s
    def PRGA(self,S):
        i,j = 0,0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # swap

            K = S[(S[i] + S[j]) % 256]
            yield K

# Test vectors  https://en.wikipedia.org/wiki/RC4 :

streamcipher = RC4("Key")
#Key = Key 	
#Keysteam = EB9F7781B734CA72A719… 	

# streamcipher = RC4("Wiki")
#Key = Wiki 	
#Keysteam = 6044DB6D41B7 	

# streamcipher = RC4("Secret")
# Key = Secret 	
# Keysteam = 04D46B053CA87B59 	


keystream = streamcipher.key
#format integers to hex for comperason. 
for c in range(10):
    print("%02X" % (next(keystream)),end='')




