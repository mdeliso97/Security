import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes


def ecb(label):
    # Key and plaintext
    key = get_random_bytes(16)  # 128-bit key
    plaintext = b"This is the plaintext message"

    # Create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    return label.config(text="Button ecb!")


def ecb_encrypt(key, message, cipher):
    # Encryption
    padded_plaintext = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return


def ecb_decrypt(key, message, cipher):
    # Decryption
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(decipher.decrypt(message), AES.block_size)
    return
