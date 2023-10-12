import json

from GCM import *


def rsa_oaep_encryption(file, json_pub):
    # Retrieve GCM AEAD cipher's outputs
    json_output, key = gcm_encryption(file)

    json_file = json.loads(json_output)
    json_pub = json.loads(json_pub)

    n_key = decoding64(json_pub['n'])
    pub_key = decoding64(json_pub['public'])

    # ToDo: M < n, C = M^e (mod n)
    # cipher = AES.new(pub_key, AES.MODE_GCM, nonce=nonce_key)
    # key_encrypt = cipher.encrypt_and_digest(key)

    if len(str(file)) < len(str(n_key)):
        key_encrypt = pow(file, pub_key, n_key)
    else:
        return print("error occurred: length not respected -> M < n")

    return json_output, key_encrypt


def rsa_oaep_decryption(json_file, key_encrypt, json_key):
    json_file = json.loads(json_file)
    json_key = json.loads(json_key)

    # tag_key = decoding64(json_file['tag'])
    n_key = decoding64(json_key['n'])
    private_key = decoding64(json_key['private'])
    ct_key = decoding64(json_file['ciphertext'])

    # ToDo: C = ciphertext, M = C^d (mod n)
    pub_decrypt_key = pow(key_encrypt, private_key, n_key)



    file_decrypted = pow(ct_key, pub_decrypt_key, n_key)

    # key_decipher = AES.new(key_private, AES.MODE_GCM, nonce=nonce_key)
    # key_decrypted = key_decipher.decrypt_and_verify(key_encrypt, tag_key)
    # file_decipher = AES.new(key_decrypted, AES.MODE_GCM, nonce=nonce_key)
    # file_decrypted = file_decipher.decrypt_and_verify(ct_key, tag_key)

    return file_decrypted
