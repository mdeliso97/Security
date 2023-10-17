import hashlib
import json
import os
import random

from Crypto.Random import get_random_bytes

from Utilities import codificator
from math import ceil
from Ciphers.GCM import gcm_encrypt, gcm_decrypt

'''
This class defines the logic implemented by hand of RSA-OAEP asymmetric encryption and decryption using GCM AEAD cipher
as symmetric cipher. 
'''


# converts a non-negative integer to an octet string of a specified length
def i2osp(x: int, xlen: int) -> bytes:
    return x.to_bytes(xlen, byteorder='little')


def mgf1_mask(seed: bytes, message_length: int) -> bytes:
    '''MGF1 mask generation function with SHA-1'''
    t = b''
    hash_length = len(sha1_hash(b''))
    for c in range(0, ceil(message_length / hash_length)):
        _c = i2osp(c, 4)
        t += sha1_hash(seed + _c)
    return t[:message_length]


def sha1_hash(message: bytes) -> bytes:
    '''SHA-1 hash function'''
    hasher = hashlib.sha1()
    hasher.update(message)
    return hasher.digest()


# performs a bitwise XOR operation between two byte sequences: data and mask
def xor_operation(data, mask):
    masked = b''
    length_data = len(data)
    length_mask = len(mask)
    for i in range(max(length_data, length_mask)):
        if i < length_data and i < length_mask:
            masked += (data[i] ^ mask[i]).to_bytes(1, byteorder='little')
        elif i < length_data:
            masked += data[i].to_bytes(1, byteorder='little')
        else:
            break
    return masked


# RSA-OAEP encryption using GCM cipher
def rsa_oaep_encryption(file, json_pub):
    BLOCK_SIZE = 32

    # retrieve n and public key for encryption
    json_pub = json.loads(json_pub)

    n_key = json_pub['n']
    pub_key = json_pub['public']

    label = b''

    password = None

    label_hash = sha1_hash(label)

    ps = b'\x00' * (len(n_key) - len(file) - 2 * len(label_hash) - 2)  # a byte string of k − m L e n − 2 ⋅ h L e n − 2

    file_db = label_hash + ps + b'\x01' + file

    seed = os.urandom(len(label_hash))

    db_mask = mgf1_mask(seed, len(n_key) - len(label_hash) - 1)

    file_masked = xor_operation(file_db, db_mask)

    seed_mask = mgf1_mask(file_masked, len(label_hash))

    masked_seed = xor_operation(seed, seed_mask)

    file_oaep = b'\x00' + masked_seed + file_masked

    # retrieve GCM AEAD cipher's outputs: ciphertext, nonce, tag and key
    json_output, key = gcm_encrypt(file_oaep, password)

    # convert GCM key from integer into byte string
    key = int.from_bytes(key, byteorder='little')

    # key encryption: M < n, C = M^e (mod n)
    if len(str(key)) < len(str(n_key)):
        key_encrypt = pow(key, pub_key, n_key)
    else:
        return print("error occurred: length not respected -> M < n")

    return json_output, key_encrypt


# RSA-OAEP decryption using GCM cipher
def rsa_oaep_decryption(json_file, key_encrypt, json_key_private):



    return key_decrypted
