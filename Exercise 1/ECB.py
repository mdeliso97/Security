from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from codificator import *


# ToDo: key + message bytes
def ecb_encrypt(file):
    BLOCK_SIZE = 32  # Bytes

    key = get_random_bytes(BLOCK_SIZE)

    # Create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    print("encrypt!")
    # Encryption
    encrypted_text = cipher.encrypt(pad(file, BLOCK_SIZE))

    return encrypted_text, key


def ecb_decrypt(message, key):
    BLOCK_SIZE = 32  # Bytes
    print("decrypt!")

    # Decryption
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = decipher.decrypt(message)
    decrypted_text = unpad(decrypted_text, BLOCK_SIZE)

    return decrypted_text
