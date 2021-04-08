import random
from Crypto.Util import number

#euclids greatest common divisor
def egcd(a, b):
    x = 0 
    y = 1
    u = 1
    v = 0
    while a != 0:
        q = b//a 
        r = b % a
        m = x-u*q
        n = y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
    return gcd, x, y


#Generate the public and private keys
def gen_keys(p, q):
    e = 65537
    n = p * q
    phi = (p - 1) * (q - 1)
    gcd, d, b = egcd(e, phi)
    # Keys:((pub),  (priv))
    return ((e, n), (d, n))

#Encode the message
def encode(key, p):
    e, n = key
    cipher = [pow(ord(char), e, n) for char in p]
    return cipher

#generate 512 bit primes
n_length = 512
p = number.getPrime(n_length)
q = number.getPrime(n_length)

#generate the keys for the message
msg_key = gen_keys(p, q)

msg = "*REDACTED*"

#print the public key (e and n)
print("Public key:")
print(msg_key[0])

msg_c=(encode(msg_key[0], msg))

#print the encoded message
print("Encrypted message:")
print(msg_c)


