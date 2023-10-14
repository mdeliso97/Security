import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from codificator import *

'''
This class defines the logic of CBC symmetric encryption and decryption. 
'''


# CBC encryption
def encrypt_cbc(file):
    BLOCK_SIZE = 32  # Bytes

    # generate random 256-bit key
    key = get_random_bytes(BLOCK_SIZE)

    # create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)

    # perform padding and encrypt plaintext
    encrypted_text = cipher.encrypt(pad(file, BLOCK_SIZE))

    # generate initialization vector and convert to string both initialization vector and ciphertext
    iv_key = encoding64(cipher.iv)
    ct_key = encoding64(encrypted_text)

    json_output = json.dumps({'iv': iv_key, 'ciphertext': ct_key})

    return json_output, key


# CBC decryption
def decrypt_cbc(json_file, key):
    BLOCK_SIZE = 32  # Bytes

    json_file = json.loads(json_file)

    # retrieve initialization vector and ciphertext from json file
    iv_key = decoding64(json_file['iv'])
    ct_key = decoding64(json_file['ciphertext'])

    # define AES decipher in CBC mode with initialization vector and key
    decipher = AES.new(key, AES.MODE_CBC, iv_key)

    # decrypt ciphertext
    decrypted_file = decipher.decrypt(ct_key)

    # unpad decrypted ciphertext
    decrypted_file = unpad(decrypted_file, BLOCK_SIZE)

    return decrypted_file

