### Why using ECB is a bad idea

- It is easy to decrypt the message without the need of the key
- ECB mode encrypts each block of data independently, without taking into account the surrounding context. As a result, identical plaintext blocks are encrypted into identical ciphertext blocks. This lack of diffusion means that patterns and repeating data in the plaintext are preserved in the ciphertext.
- Because identical plaintext blocks produce identical ciphertext blocks, an attacker can perform frequency analysis on the ciphertext to identify repeating patterns or common elements. This is because there are a limited number of possible input blocks, making it easier for an attacker to perform exhaustive searches or other attacks to recover the plaintext.
- ECB mode only provides confidentiality and does not include any authentication mechanism.
- E.g. An encrypted image can still be readable because the same patterns will be encrypted in the same way and the image will most likely belong readable.
- ECB mode only provides confidentiality and does not include any authentication mechanism. This means that an attacker can modify the ciphertext, and the recipient will have no way of detecting the tampering.


### AEAD is better than “classic” modes of operation

- AEAD is better than “classic” modes of operationAEAD modes like GCM, CCM, or EAX combine encryption and authentication in a single step. Classic modes, such as ECB or CBC, require separate mechanisms for encryption and integrity checking (e.g., HMAC), making the implementation more complex and potentially error-prone.
- AEAD modes use cryptographic tags to detect any unauthorized changes to the ciphertext. In classic modes, without authentication, an attacker can tamper with the ciphertext or manipulate the data without detection.
- AEAD avoids Man in the middle attack




