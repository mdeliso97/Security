from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

'''
This class defines the logic of ECB symmetric encryption and decryption.
'''


# ECB encryption
def ecb_encrypt(file):
    BLOCK_SIZE = 32  # Bytes

    # randomize key for encryption and decryption
    key = get_random_bytes(BLOCK_SIZE)

    # create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    # perform padding and after encrypt plaintext
    encrypted_text = cipher.encrypt(pad(file, BLOCK_SIZE))

    return encrypted_text, key


# ECB decryption
def ecb_decrypt(message, key):
    BLOCK_SIZE = 32  # Bytes

    # define ECB decipher with key
    decipher = AES.new(key, AES.MODE_ECB)

    # decrypt ciphertext
    decrypted_text = decipher.decrypt(message)

    # unpad decrypted ciphertext
    decrypted_text = unpad(decrypted_text, BLOCK_SIZE)

    return decrypted_text
