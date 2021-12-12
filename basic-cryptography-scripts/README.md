# [🐳](https://mithi.github.io/deep-blueberry) [☕️](https://ko-fi.com/minimithi)

# About
- Python scripts that illustrate basic cryptography concepts based on Coursera Standford Cryptography I course and more
- Each has tests, notes and detailed explanations in the hopes that you can clearly understand what's happening
- The references section of this README links to awesome websites you can use for learning cryptography

### 1. [Many Time Pad](./01-many-time-pad/)
- This script will be able to decrypt a target ciphertext, given a bunch on intercepted ciphertexts encrypted with the same key (which may or may not have random errors). A stream cipher key should never be used more than once.

### 2. [Block Ciphers](./02-block-ciphers/)
- You'll be able to encrypt or decrypt a message given a key using two modes of block cipher operations; CBC mode and CTR mode.

### 3. [Simple File Authentication System](./03-file-authentication/)
- A simple file authentication system that simulate how you'd be able to authenticate and play video chunks as they are downloaded without having to wait for the entire file.

### 4. [Padding Oracle Attack](./04-padding-oracle/)
- This script illustrates how you'd be able to decrypt an intercepted ciphertext if the receiver reveals whether a sent ciphertext is of valid format or not.

### 5.  [Meet In the Middle Attack](./05-meet-in-the-middle/)
- The meet-in-the-middle attack (MITM) is a generic space–time tradeoff cryptographic attack. We demonstrate the MITM attack by using it to solve a discrete log problem.

### 6. [Factoring Challenges](./06-factoring/)
- RSA can be broken when the public modulus `N` is generated incorrectly. These scripts illustrate how you'd be able to factor `N` when `p` and `q` are close to each other.

### 7. [Basic RSA](./07-basic-rsa/)
 - An example pipeline that demonstrates basic RSA encryption and decryption.
 
# References
- [❤️ Crypto Hack](https://cryptohack.org/)
- [Coursera Cryptography I, Stanford, Dan Boneh](https://www-origin.coursera.org/learn/crypto)
- [A Graduate Course in Applied Cryptography by Dan Boneh and Victor Shoup](https://toc.cryptobook.us/)
- [Crypto 101 by Laurens Van Houtven](https://www.crypto101.io/)
- [Crypto Pals Crypto Challenges](https://cryptopals.com/)

# [🐳](https://mithi.github.io/deep-blueberry) [☕️](https://ko-fi.com/minimithi)
