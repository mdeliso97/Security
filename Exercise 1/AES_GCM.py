from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def AES_GCM_encryption():
    # Generate a random 256-bit key
    key = get_random_bytes(32)

    # Initialize the AES-GCM cipher with the key
    cipher = AES.new(key, AES.MODE_GCM)

    # Message to be encrypted
    message = b"Hello, World!"

    # Encrypt the message
    ciphertext, tag = cipher.encrypt_and_digest(message)

    # Print the ciphertext and tag (used for authentication)
    print("Ciphertext:", ciphertext.hex())
    print("Tag:", tag.hex())

    # Decrypt the ciphertext
    decipher = AES.new(key, AES.MODE_GCM, nonce=cipher.nonce)
    plaintext = decipher.decrypt_and_verify(ciphertext, tag)

    # Print the decrypted message
    print("Decrypted Message:", plaintext.decode("utf-8"))


def AES_GCM_decryption(message, key, tag):
    # Decrypt the ciphertext

    # Initialize the AES-GCM cipher with the key
    cipher = AES.new(key, AES.MODE_GCM)

    decipher = AES.new(key, AES.MODE_GCM, nonce=cipher.nonce)
    plaintext = decipher.decrypt_and_verify(message, tag)

    # Print the decrypted message
    print("Decrypted Message:", plaintext.decode("utf-8"))
