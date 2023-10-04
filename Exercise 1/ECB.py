import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes


def ecb(message, is_encrypt):

    # Key and plaintext
    key = get_random_bytes(16)  # 128-bit key

    message = message.encode('utf-8')

    # Create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    if is_encrypt.get():
        message = ecb_encrypt(message, cipher)
    else:
        message = ecb_decrypt(message, key)

    return message, key


def ecb_encrypt(message, cipher):
    print("encrypt!")
    # Encryption
    padded_plaintext = pad(message, AES.block_size)
    encrypted_text = cipher.encrypt(padded_plaintext)
    return encrypted_text


def ecb_decrypt(message, key):
    print("decrypt!")
    # Decryption
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(decipher.decrypt(message), AES.block_size)
    return decrypted_text
