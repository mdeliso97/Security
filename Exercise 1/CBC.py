import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def cbc(message, is_encrypt):
    # data = b"secret"

    # Key
    key = get_random_bytes(16)  # 128-bit key

    # Create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)

    if is_encrypt.get():
        message = encrypt_cbc(message, cipher)
    else:
        message = decrypt_cbc(key, message)

    return message, key


def encrypt_cbc(message, cipher):
    print("encrypt!")
    # Encryption

    ct_bytes = cipher.encrypt(pad(message, AES.block_size))

    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')

    result = json.dumps({'iv': iv, 'ciphertext': ct})

    print(result)

    return result


def decrypt_cbc(key, message_encrypted):
    try:
        b64 = json.loads(message_encrypted)

        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])

        decipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(decipher.decrypt(ct), AES.block_size)
        print("The message was: ", pt)
        return pt

    except (ValueError, KeyError):
        print("Incorrect decryption")
