class RC4: 
    def __init__(self,key): 
       #returns list of ints of given length
       self.key =  self.PRGA( self.KSA(list(key.encode())),10)
       
       #returns generator that can generate one word of the keystream a time without given limit
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

    def PRGA(self,S,n):
        i,j = 0,0
        key=[]
        for i in (range(n)):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # swap
            key.append( S[(S[i] + S[j]) % 256] )
        return key

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

#get keystream generator
keystream = streamcipher.keygenerator
#format integers to hex for comperason. 
for c in range(10):
    print("%02X" % (next(keystream)),end='')


print("",end='\n')

#get keystream. 
keystream = streamcipher.key
#format integers to hex for comperason. 
for c in keystream:
    print("%02X" % (c),end='')


