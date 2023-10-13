### Demonstration showing why using ECB is a bad idea

- It is easy to decrypt the message without the need of the key
- ECB mode encrypts each block of data independently, without taking into account the surrounding context. As a result, identical plaintext blocks are encrypted into identical ciphertext blocks. This lack of diffusion means that patterns and repeating data in the plaintext are preserved in the ciphertext.
- Because identical plaintext blocks produce identical ciphertext blocks, an attacker can perform frequency analysis on the ciphertext to identify repeating patterns or common elements. This is because there are a limited number of possible input blocks, making it easier for an attacker to perform exhaustive searches or other attacks to recover the plaintext.
- ECB mode only provides confidentiality and does not include any authentication mechanism.
- E.g. An encrypted image can still be readable because the same patterns will be encrypted in the same way and the image will most likely belong readable.
- 

### Demonstration showing that AEAD is better than “classic” modes of operation

- 