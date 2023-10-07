import json
from Crypto.Util.Padding import unpad, pad
from codificator import *
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def GCM_encryption(file):
    BLOCK_SIZE = 32  # Bytes

    # Generate a random 256-bit key
    key = get_random_bytes(BLOCK_SIZE)

    # Generate a random 96-bit key
    nonce_key = get_random_bytes(12)  # 96 bits = 12 bytes (AES-GCM requires a 12-byte nonce)

    # Initialize the AES-GCM cipher with the key
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce_key)

    # Encrypt the message
    ct_key, tag_key = cipher.encrypt_and_digest(file)

    # ct_key = pad(ct_key, BLOCK_SIZE)

    tag_key = encoding64(tag_key)
    ct_key = encoding64(ct_key)
    nonce_key = encoding64(nonce_key)

    json_output = json.dumps({'nonce': nonce_key, 'tag': tag_key, 'ciphertext': ct_key})

    return json_output, key


def GCM_decryption(json_file, key):
    BLOCK_SIZE = 32  # Bytes

    # Decrypt the ciphertext

    # Extract nonce, tag and encrypted file
    json_file = json.loads(json_file)

    nonce_key = decoding64(json_file['nonce'])
    tag_key = decoding64(json_file['tag'])
    ct_key = decoding64(json_file['ciphertext'])

    decipher = AES.new(key, AES.MODE_GCM, nonce=nonce_key)

    decrypted_file = decipher.decrypt_and_verify(ct_key, tag_key)
    # decrypted_file = unpad(decrypted_file, BLOCK_SIZE)

    return decrypted_file
