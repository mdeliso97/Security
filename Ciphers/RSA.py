import json
from Ciphers.GCM import gcm_encrypt, gcm_decrypt
from Utilities import codificator

'''
This class defines the logic implemented by hand of RSA asymmetric encryption and decryption using GCM AEAD cipher as 
symmetric cipher. 
'''


# RSA encryption using GCM cipher
def rsa_encryption(file, json_pub):
    password = None

    # retrieve GCM AEAD cipher's outputs: ciphertext, nonce, tag and key
    json_output, key = gcm_encrypt(file, password)

    json_pub = json.loads(json_pub)

    # retrieve n and public key for encryption
    n_key = json_pub['n']
    pub_key = json_pub['public']

    # convert GCM key from integer into byte string
    key = int.from_bytes(key, byteorder='little')

    # key encryption: M < n, C = M^e (mod n)
    if len(str(key)) < len(str(n_key)):
        key_encrypt = pow(key, pub_key, n_key)
    else:
        return print("error occurred: length not respected -> M < n")

    return json_output, key_encrypt


# RSA decryption using GCM cipher
def rsa_decryption(json_file, key_encrypt, json_key_private):
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
    key_decrypted = gcm_decrypt(json_file, decrypt_key)

    return key_decrypted
