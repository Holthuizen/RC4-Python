#RC4 Python

**This repository contains a Python implementation of RC4.** 

##Intorduction

RC4 was designed in 1987 by Ron Rivest of RSA Security. RC4 has been one of the most used stream cipher from its release in 1994 until 2014.  It saw implementation in many protocols like SSH, TSL, WEP etc.  Even though it is vulnerable to crypto-analyses as result of relations between input (secret key) and output (keystream), it managed to be of use for 20 years, when many other alternatives could not. Google and Microsoft dropped support for RC4 in 2015 after researchers managed to decrypt a cooky send over TSL with RC4 in (just) 52 hours.   

RC4 can be though of as a software implementation of the classic Single Rotary encryption (found in the enigma) with a few modifications to significantly improve its security while remaining its simplicity. The most important improvement of RC4 is that it has an initial state of 256 bytes, witch theoretically results in an enormous state space. Not going into the math, to guess all the 8 bit numbers in the correct order from its 256 long array, you theoretically need 256^256 max guesses, with is unfeasible with current technology.
