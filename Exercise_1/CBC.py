import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

import codificator
from codificator import *

'''
This class defines the logic of CBC symmetric encryption and decryption. 
'''


# CBC encryption
def cbc_encrypt(file, password):
    BLOCK_SIZE = 32  # Bytes

    if password is None:
        # randomize key for encryption and decryption
        key = get_random_bytes(BLOCK_SIZE)
    else:
        password = codificator.decoding64(password)
        key = pad(password, BLOCK_SIZE)

    # create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)

    # perform padding and encrypt plaintext
    encrypted_text = cipher.encrypt(pad(file, BLOCK_SIZE))

    # generate initialization vector and convert to string both initialization vector and ciphertext
    iv_key = encoding64(cipher.iv)
    ct_key = encoding64(encrypted_text)

    json_output = json.dumps({'iv': iv_key, 'ciphertext': ct_key})

    if password is None:
        return json_output, key
    else:
        return json_output


# CBC decryption
def cbc_decrypt(json_file, key):
    BLOCK_SIZE = 32  # Bytes

    if not isinstance(key, (bytes, bytearray)):
        key = codificator.decoding64(key)
        key = pad(key, BLOCK_SIZE)

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
