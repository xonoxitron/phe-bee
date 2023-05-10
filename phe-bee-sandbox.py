from prime import *
import random

# encryption function


def encrypt(m, r, exponential=False):
    c1 = pow(g, r, p)
    if exponential is True:
        c2 = (pow(g, m, p) * pow(y, r, p)) % p
    else:
        c2 = (m * pow(y, r, p)) % p
    return c1, c2

# decryption function


def decrypt(c1, c2):
    return (c2 * pow(c1, -1*x, p)) % p


# key generation
p = generate_random_prime_number(bits=1024)
g = generate_random_prime_number(bits=64)

x = generate_random_prime_number(bits=512)  # private key
y = pow(g, x, p)                            # public key

print(x, y)

m = 100                                     # message to encrypt
r = random.randint(1, p-1)                  # random encryption number

print(m, r)

c1, c2 = encrypt(m, r)
p = decrypt(c1, c2)

print(c1, c2, p)

# multiplicative homomorphic
m1 = 9
m2 = 11

r1 = random.randint(1, p-1)
r2 = random.randint(1, p-1)

m1_encrypted = encrypt(m1, r1)
m2_encrypted = encrypt(m2, r2)

h1 = encrypt(m1*m2, r1+r2)
h2 = m1_encrypted[0]*m2_encrypted[0] % p, m1_encrypted[1]*m2_encrypted[1] % p

print(h1, h2)
assert h1 == h2


# additive homomorphic
m1_encrypted = encrypt(m1, r1, exponential=True)
m2_encrypted = encrypt(m2, r2, exponential=True)

h1 = encrypt(m1+m2, r1+r2, exponential=True)
h2 = m1_encrypted[0]*m2_encrypted[0] % p, m1_encrypted[1]*m2_encrypted[1] % p

print(h1, h2)
assert h1 == h2
