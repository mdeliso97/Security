import hashlib
import json
import os

from Utilities import codificator
from math import ceil
from Ciphers.GCM import gcm_encrypt, gcm_decrypt

'''
This class defines the logic implemented by hand of RSA-OAEP asymmetric encryption and decryption using GCM AEAD cipher
as symmetric cipher. 
'''


# defines the MGF1 mask using SHA-1 hash function
def mgf1_mask(seed, message_length):
    t = b''
    hash_length = len(sha1_hash(b''))
    for c in range(0, ceil(message_length / hash_length)):
        _c = c.to_bytes(4, byteorder='little')
        t += sha1_hash(seed + _c)
    return t[:message_length]


# defines the hash function used for the mask SHA-1
def sha1_hash(message: bytes) -> bytes:
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
    # retrieve n and public key for encryption
    json_pub = json.loads(json_pub)

    n_key = json_pub['n']
    pub_key = json_pub['public']

    label = b''

    password = None

    # label to be associated with the message which is used to authenticate data
    label_hash = sha1_hash(label)

    # generate a padding string PS
    ps = b'\x00' * (len(str(n_key)) - len(file) - 2 * len(label_hash) - 2)  # a byte string of k − mLen − 2 ⋅ hLen − 2

    # concatenate lHash, PS, the single byte 0x01
    file_db = label_hash + ps + b'\x01' + file

    # generate a random seed of same length of label hash
    seed = os.urandom(len(label_hash))

    # generate a mask of the appropriate length for the data block
    db_mask = mgf1_mask(seed, len(str(n_key)) - len(label_hash) - 1)

    # mask the data block with the generated mask
    file_masked = xor_operation(file_db, db_mask)

    # use the mask generating function to generate a mask of label hash length for the seed
    seed_mask = mgf1_mask(file_masked, len(label_hash))

    # mask the seed with the generated mask
    masked_seed = xor_operation(seed, seed_mask)

    # concatenate everything to obtain encoded file
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
    json_key = json.loads(json_key_private)

    # retrieve n and private key for decryption of key
    private_key = json_key["private"]
    n_key = json_key['n']

    # convert string encrypted key into integer key
    key_encrypt = int(key_encrypt)

    # key decryption: C = ciphertext, M = C^d (mod n)
    decrypt_key = pow(key_encrypt, private_key, n_key)

    # convert decrypted GCM key from integer to byte string
    decrypt_key = codificator.decoding64(decrypt_key)

    # decrypt ciphertext with GCM AEAD using decrypted key
    file_decrypted = gcm_decrypt(json_file, decrypt_key)

    # oaep revert masking + hashing
    label = b''

    label_hash = sha1_hash(label)

    _, masked_seed, masked_db = file_decrypted[:1], file_decrypted[1:1 + len(label_hash)], file_decrypted[
                                                                                           1 + len(label_hash):]

    seed_mask = mgf1_mask(masked_db, len(label_hash))

    seed = xor_operation(masked_seed, seed_mask)

    db_mask = mgf1_mask(seed, len(str(n_key)) - len(label_hash) - 1)

    file_masked = xor_operation(masked_db, db_mask)

    _label_hash = file_masked[:len(label_hash)]
    assert label_hash == _label_hash  # check if label corresponds
    i = len(label_hash)
    while i < len(file_masked):
        if file_masked[i] == 0:
            i += 1
            continue
        elif file_masked[i] == 1:
            i += 1
            break
        else:
            raise Exception()
    file_raw = file_masked[i:]
    return file_raw
