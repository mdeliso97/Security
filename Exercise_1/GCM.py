import json
from codificator import *
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def gcm_encryption(file):
    # Generate a random 256-bit key
    key = get_random_bytes(32)

    # Generate a random 96-bit key
    nonce_key = get_random_bytes(12)  # 96 bits = 12 bytes (AES-GCM requires a 12-byte nonce)

    # Initialize the AES-GCM cipher with the key
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce_key)

    # Encrypt the message
    key_ct, key_tag = cipher.encrypt_and_digest(file)

    tag_key = encoding64(key_tag)
    ct_key = encoding64(key_ct)
    nonce_key = encoding64(nonce_key)

    json_output = json.dumps({'nonce': nonce_key, 'tag': tag_key, 'ciphertext': ct_key})

    return json_output, key


def gcm_decryption(json_file, key):
    # Extract nonce, tag and encrypted file
    json_file = json.loads(json_file)

    key_nonce = decoding64(json_file['nonce'])
    key_tag = decoding64(json_file['tag'])
    key_ct = decoding64(json_file['ciphertext'])

    decipher = AES.new(key, AES.MODE_GCM, nonce=key_nonce)

    file_decrypted = decipher.decrypt_and_verify(key_ct, key_tag)

    return file_decrypted
