import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes


def ecb(message, is_encrypt):
    # Key and plaintext
    key = get_random_bytes(16)  # 128-bit key

    # Create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    if is_encrypt:
        message = ecb_decrypt(message, cipher)
    else:
        message = ecb_decrypt(key, message)

    return message


def ecb_encrypt(message, cipher):
    print("encrypt!")
    # Encryption
    padded_plaintext = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext


def ecb_decrypt(key, message):
    print("decrypt!")
    # Decryption
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(decipher.decrypt(message), AES.block_size)
    return decrypted_text
