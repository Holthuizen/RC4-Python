# RC4 Python

**This repository contains a Python implementation of RC4.** 

For a Node JS version check my gist: https://gist.github.com/Holthuizen/a84c12038f4cec47d9264d69c23db4da 

# RC4-Python 
RC4 stream cipher
This repository contains two RC4 implementations in python. The first is an exact copy of the in 1994 leaked algorithm that was designed in 1987 by Ron Rivest of RSA Security. 
The second proposes a modification to the Key-scheduling algorithm (KSA) to theoretically improve entropy of the initial state, reducing the effectiveness of current crypto analysis on RC4. The modified file is still WIP and is presented as .ipynb file (jupyter notebook).

## Introduction:

At the beginning of this century, RC4 was the most used stream cipher. It saw implementations in wireless security (WEP), browser-based encryption SSL and TSL and the secure shell SSH protocol. Its fame was short-lived; within one decade various papers were published showing all kinds of patterns in its supposedly random output stream, making it vulnerable to crypto analysis. In 2015, Google went as far as banning protocols that implemented RC4 from the Chrome browser.
In this repository I will propose a modification of RC4 that improves on a few significant weaknesses. Pleas do keep in mind that I cannot recommend implementing this version. The only way to determine the safety of a cipher is by extensive research and testing. I designed this modification only for my own interest and will probably only use it for hobby projects with a low priority for security.  

## Motivation: 

RC4 popularity was no coincidence. The steam cipher has many advantages over most alternatives from its time. RC4 is very vast and well-suited as software implementation. It is ideal for broad deployment since you don’t have to consider special hardware to be able to run this encryption algorithm, unlike with for example the Advanced Encryption Standard (AES). But the most appealing aspects of RC4 are probably its simplicity and clever design. The algorithm can be implemented in only a few lines of code and can operate completely independently from its environment. The algorithm doesn’t rely on a randomly generated initialization vector but only on a secret key. 
RC4 is a very flexible algorithm, even though there are only a few commonly used standard protocols. rfc4345 is the most used one and dictates a key of 128 or 256 bits long, and a dump of the first 1536 bytes of a keystream. RC4 is based around internal state array S. The smaller the state array, the faster the algorithm will be at the cost of security. By convention this array is almost always 256 bytes long. 
RC4 can be split up in 2 sub algorithms, namely, KSA or Key-scheduling-algorithm and Pseudo-random generation algorithm (PRGA). We will only focus on KSA since most of the security problems are related to this portion of RC4 and this is where I will propose a tweaked strategy. 

## RC4 mechanics in short: 
KSA is run once to setup the cipher. It creates an array of 256 bytes. Initially, the array is filled with numbers equal to their index. Starting at 0, 1, 2, 3 etc. all the way up to 255. Then a key is introduced, usually an array of bytes in decimal representation.
Then, the array is mixed and shuffled with the key, in a pseudorandom order. The same key will always give the same output, but a small change in the key will give a vastly different result. This permutated array is the output of the KS algorithm and is called the secret internal state, denoted by capital S. At this point KSA is finished and PRGA takes the secret state S and produces one word (a byte) at a time, constantly updating S to keep its structure random and secret. The produced words form its keystream. This keystream must remain secret, and will be used to encrypt plain text into cipher text via an XOR operation. 
## Security: 
Since RC4 produces a way less random output than initially thought, an attacker can, when collecting enough output, guess the initial state of S and therefore also determine the secret key. To pull this off an attacker needs a lot of data to look for patterns that can help break the encryption. For example, when an encrypted message contains a lot of repeated words, like http headers or usernames.   
To combat this, we can improve the randomness and entropy of the initial state S by using more than one key. For this implementation I will demonstrate the use of 2 keys. We can further increase the difficulty to guess the key(s) by deleting a part of the output S that KSA produces.

## KSA modification: 
The new algorithm works as follows: 
We still use the original KS algorithm and run it twice, with a separate key for each run, resulting in two 256-byte arrays, S1 and S2. Then we mix S1 and S2 to form S3, this is achieved by only taking the numbers at odd indexes from S1 and even indexes from S2. The resulting 256-byte array S3 will only contain 50% of the data from S1 + S2 respectively. The loss off data makes it extremely hard to distill the used keys from RC4s initial output.  
