from GCM import *


def rsa_oaep_encryption(file, json_pub):

    # Retrieve GCM AEAD cipher's outputs
    json_output, key = GCM_encryption(file)

    json_file = json.loads(json_output)
    json_pub = json.loads(json_pub)

    nonce_key = decoding64(json_file['nonce'])
    pub_key = json.loads(json_pub['public'])

    cipher = AES.new(pub_key, AES.MODE_GCM, nonce=nonce_key)

    key_encrypt = cipher.encrypt_and_digest(key)

    return json_output, key_encrypt


def rsa_oaep_decryption(json_file, key_encrypt, key_private):

    json_file = json.loads(json_file)

    nonce_key = decoding64(json_file['nonce'])
    tag_key = decoding64(json_file['tag'])
    ct_key = decoding64(json_file['ciphertext'])

    key_decipher = AES.new(key_private, AES.MODE_GCM, nonce=nonce_key)

    key_decrypted = key_decipher.decrypt_and_verify(key_encrypt, tag_key)

    file_decipher = AES.new(key_decrypted, AES.MODE_GCM, nonce=nonce_key)

    file_decrypted = file_decipher.decrypt_and_verify(ct_key, tag_key)

    return file_decrypted
