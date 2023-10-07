from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from codificator import *


# ToDo: key + message bytes
def ecb_encrypt(message):
    BLOCK_SIZE = 32  # Bytes

    key = get_random_bytes(32)

    # key = 'abcdefghijklmnop'

    # message = encoding64(message)

    # key = encoding64(key)

    # Create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    print("encrypt!")
    # Encryption
    encrypted_text = cipher.encrypt(pad(message, BLOCK_SIZE))
    #padded_plaintext = pad(message, AES.block_size)
    #encrypted_text = cipher.encrypt(padded_plaintext)
    # key = encoding64(key)

    return encrypted_text, key


def ecb_decrypt(message, key):
    BLOCK_SIZE = 32  # Bytes
    print("decrypt!")

    # key = 'abcdefghijklmnop'

    # message = message.encode('utf-8')

    # key = decoding64(key)
    # key = decoding64(key)
    # Decryption
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = decipher.decrypt(message)
    decrypted_text = unpad(decrypted_text, BLOCK_SIZE)
    # decrypted_text = unpad(message, BLOCK_SIZE)
    # decrypted_text = decipher.decrypt(decrypted_text)
    return decrypted_text
