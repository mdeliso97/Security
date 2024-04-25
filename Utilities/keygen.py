import json
import math
from Crypto.Util import number

'''
This class keygen is attached to the button "keygen" in the GUI and is responsible of generating the key pairs public 
and private key. It follows the following steps:

1. Select two large prime numbers, p and q.
2. Calculate the modulus n = p * q.
3. Calculate Euler's totient function phi(n) = (p - 1) * (q - 1).
4. Choose a public exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1 (e is usually a small prime like 65537).
5. Calculate the private exponent d such that d * e ≡ 1 (mod phi(n)).
6. The public key is (n, e) and the private key is (n, d).
'''


# outputs the key as json files
def keygen_output(json_output_public: json, json_output_private: json):
    with open("public_key.json", "w") as output_file:
        output_file.write(json_output_public)

    with open("private_key.json", "w") as output_file:
        output_file.write(json_output_private)


# generates private and public keys
def keygen():
    # generate two big prime numbers of 3000 length
    p = number.getPrime(3000)
    q = number.getPrime(3000)
    # calculate modulus n
    n = p * q

    # calculate Euler's Totient function
    phi = (p - 1) * (q - 1)

    # generate exponent e
    # e = 65537
    e = 0

    while math.gcd(e, phi) != 1:
        e = number.getPrime(50)

    # generate d
    d = pow(e, -1, phi)

    json_output_public = json.dumps({'n': n, 'public': e})
    json_output_private = json.dumps({'n': n, 'private': d})

    return keygen_output(json_output_public, json_output_private)
