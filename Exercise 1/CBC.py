import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from codificator import *


def encrypt_cbc(file):
    BLOCK_SIZE = 32  # Bytes
    print("encrypt!")
    # Encryption

    # Key
    key = get_random_bytes(BLOCK_SIZE)  # 256-bit key

    # Create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)

    encrypted_text = cipher.encrypt(pad(file, BLOCK_SIZE))

    iv_key = encoding64(cipher.iv)
    ct_key = encoding64(encrypted_text)

    json_output = json.dumps({'iv': iv_key, 'ciphertext': ct_key})

    print(json_output)

    return json_output, key


def decrypt_cbc(json_file, key):
    BLOCK_SIZE = 32  # Bytes

    json_file = json.loads(json_file)

    iv_key = decoding64(json_file['iv'])
    ct_key = decoding64(json_file['ciphertext'])

    decipher = AES.new(key, AES.MODE_CBC, iv_key)
    decrypted_file = decipher.decrypt(ct_key)
    decrypted_file = unpad(decrypted_file, BLOCK_SIZE)

    return decrypted_file

