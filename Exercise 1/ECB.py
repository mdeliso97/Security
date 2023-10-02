import json
from base64 import b64encode
#from Crypto.Cipher import AES
#from Crypto.Util.Padding import pad
#from Crypto.Random import get_random_bytes


def ecb(label):
    # # Key and plaintext
    # key = get_random_bytes(16)  # 128-bit key
    # plaintext = b"This is the plaintext message"
    # 
    # # Create an AES cipher object in ECB mode
    # cipher = AES.new(key, AES.MODE_ECB)
    #
    # # Encryption
    # padded_plaintext = pad(plaintext, AES.block_size)
    # ciphertext = cipher.encrypt(padded_plaintext)
    #
    # # Decryption
    # decipher = AES.new(key, AES.MODE_ECB)
    # decrypted_data = unpad(decipher.decrypt(ciphertext), AES.block_size)

    return label.config(text="Button ecb!")
