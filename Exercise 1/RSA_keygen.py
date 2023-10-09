import json
import random
import math
from Crypto.Util import number
from cryptology import keygen_output

# 1. Select two large prime numbers, p and q.
# 2. Calculate the modulus n = p * q.
# 3. Calculate Euler's totient function phi(n) = (p - 1) * (q - 1).
# 4. Choose a public exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1 (e is usually a small prime like 65537).
# 5. Calculate the private exponent d such that d * e ≡ 1 (mod phi(n)).
# 6. The public key is (n, e) and the private key is (n, d).


def primes_gen(bits):
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    return p, q


def keygen():

    # generate two big prime numbers of 2048-bit length
    p, q = primes_gen(2048)

    # calculate modulus n
    n = p * q

    # calculate Euler's Totient function
    phi = (p - 1) * (q - 1)

    # generate exponent e
    e = 0

    while e < 2 and math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # generate d
    d = pow(e, -1, phi)

    json_output_public = json.dumps({'n': n, 'public': e})
    json_output_private = json.dumps({'n': n, 'private': d})

    return keygen_output(json_output_public, json_output_private)
