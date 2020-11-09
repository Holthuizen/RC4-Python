import unittest
from RC4 import RC4

class TestRC4(unittest.TestCase):
    def test_types(self): 
        ''' make sure a type error is raise when input is not of type String''' 
        self.assertRaises(TypeError,RC4,-2)
        self.assertRaises(TypeError,RC4,True)

    def test_key_not_empty(self):
        '''test to make sure key cannot be set to empty'''
        self.assertRaises(ValueError,RC4,"")
    
    def test_output(self):
        streamcipher = RC4("Wiki")	
        keystream = streamcipher.keygenerator
        output = []
        for c in range(10):
            output.append(next(keystream))
        self.assertAlmostEqual(output,[96, 68, 219, 109, 65, 183, 232, 231, 164, 214])
