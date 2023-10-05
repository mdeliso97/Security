import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes


def ecb_encrypt(message):
    BLOCK_SIZE = 32  # Bytes

    key = 'abcdefghijklmnop'

    message = message.encode('utf-8')

    # Create an AES cipher object in ECB mode
    cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)

    print("encrypt!")
    # Encryption
    encrypted_text = cipher.encrypt(pad(message, BLOCK_SIZE))
    #padded_plaintext = pad(message, AES.block_size)
    #encrypted_text = cipher.encrypt(padded_plaintext)
    return encrypted_text, key


def ecb_decrypt(message, key):
    BLOCK_SIZE = 32  # Bytes
    print("decrypt!")

    key = 'abcdefghijklmnop'

    message = message.encode('utf-8')

    # Decryption
    decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
    # decrypted_text = decipher.decrypt(message)
    # decrypted_text = unpad(decrypted_text, BLOCK_SIZE)
    decrypted_text = unpad(decipher.decrypt(message), BLOCK_SIZE)
    return decrypted_text
