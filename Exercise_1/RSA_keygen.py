import json
import random
import math

from Crypto.Util import number
from Crypto.Util.number import inverse
from cryptology import keygen_output

'''
1. Select two large prime numbers, p and q.
2. Calculate the modulus n = p * q.
3. Calculate Euler's totient function phi(n) = (p - 1) * (q - 1).
4. Choose a public exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1 (e is usually a small prime like 65537).
5. Calculate the private exponent d such that d * e ≡ 1 (mod phi(n)).
6. The public key is (n, e) and the private key is (n, d).
'''


def primes_gen(length):
    p = number.getPrime(length)
    q = number.getPrime(length)
    return p, q


def keygen():
    # generate two big prime numbers of 3000 length
    p, q = primes_gen(3000)

    print(len(str(p)))
    print(len(str(q)))

    # calculate modulus n
    n = p * q

    print(len(str(n)))

    # calculate Euler's Totient function
    phi = (p - 1) * (q - 1)

    # generate exponent e
    # e = 65537
    e = 0

    while math.gcd(e, phi) != 1:
        e = number.getPrime(50)

    # generate d
    d = inverse(e, phi)

    n_key = n
    public_key = e
    private_key = d

    json_output_public = json.dumps({'n': n_key, 'public': public_key})
    json_output_private = json.dumps({'n': n_key, 'private': private_key})

    return keygen_output(json_output_public, json_output_private)
