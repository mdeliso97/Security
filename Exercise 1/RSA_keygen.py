import json
import random
import math

from Crypto.Util import number
from Crypto.Util.number import inverse
from cryptology import keygen_output
from codificator import encoding64, decoding64

# 1. Select two large prime numbers, p and q.
# 2. Calculate the modulus n = p * q.
# 3. Calculate Euler's totient function phi(n) = (p - 1) * (q - 1).
# 4. Choose a public exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1 (e is usually a small prime like 65537).
# 5. Calculate the private exponent d such that d * e ≡ 1 (mod phi(n)).
# 6. The public key is (n, e) and the private key is (n, d).


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def primes_gen(bits):

    p = number.getPrime(bits)
    q = number.getPrime(bits)
    return p, q


def keygen():

    # generate two big prime numbers of 2048-bit length
    p, q = primes_gen(256)

    # calculate modulus n
    n = p * q

    # calculate Euler's Totient function
    phi = (p - 1) * (q - 1)

    # generate exponent e
    e = 0

    while e < 2 or math.gcd(e, phi) != 1 or not is_prime(e):
        e = random.randint(2, 1000000)

    # generate d
    d = inverse(e, phi)

    # ToDo
    n_key = decoding64(n)
    public_key = decoding64(e)
    private_key = decoding64(d)

    n_key = encoding64(n_key)
    public_key = encoding64(public_key)
    private_key = encoding64(private_key)

    json_output_public = json.dumps({'n': n_key, 'public': public_key})
    json_output_private = json.dumps({'n': n_key, 'private': private_key})

    return keygen_output(json_output_public, json_output_private)
