### Demonstration showing why using ECB is a bad idea

- It is easy to decrypt the message without the need of the key
- ECB mode encrypts each block of data independently, without taking into account the surrounding context. As a result, identical plaintext blocks are encrypted into identical ciphertext blocks. This lack of diffusion means that patterns and repeating data in the plaintext are preserved in the ciphertext.
- Because identical plaintext blocks produce identical ciphertext blocks, an attacker can perform frequency analysis on the ciphertext to identify repeating patterns or common elements. This is because there are a limited number of possible input blocks, making it easier for an attacker to perform exhaustive searches or other attacks to recover the plaintext.
- ECB mode only provides confidentiality and does not include any authentication mechanism.
- E.g. An encrypted image can still be readable because the same patterns will be encrypted in the same way and the image will most likely belong readable.
- ECB mode only provides confidentiality and does not include any authentication mechanism. This means that an attacker can modify the ciphertext, and the recipient will have no way of detecting the tampering.


### Demonstration showing that AEAD is better than “classic” modes of operation

- Demonstration showing that AEAD is better than “classic” modes of operationAEAD modes like GCM, CCM, or EAX combine encryption and authentication in a single step. Classic modes, such as ECB or CBC, require separate mechanisms for encryption and integrity checking (e.g., HMAC), making the implementation more complex and potentially error-prone.
- AEAD modes use cryptographic tags to detect any unauthorized changes to the ciphertext. In classic modes, without authentication, an attacker can tamper with the ciphertext or manipulate the data without detection.

## Instructions to getting started with the project

The Crypto 8-bit program has a main file which is called  ```cryptology.py```. The program, when started has an interactive GUI which allows Users to encrypt or decrypt by selecting their preferences between symmetric cipher and asymmetric.

The ```codificator.py``` and ```RSA_Keygen.py``` are utility classes, the first one holds methods to decode or encode from string or integer to byte format by taking the text file as input, depending on the needs. The second script becomes fundamental for the asymmetric cipher to produce keys. If the User does not have a public and private key, he can through the ```keygen``` button in the GUI generate a pair.

The other classes, namely ```CBC.py```, ```ECB.py```, ```GCM.py```, ```RSA.py``` and ```RSA_OAEP.py``` define the different ciphers' logic.

## How to run the program

#### 1. Import Project

Download the GitHub repository from GitHub.com

#### 2. Create a Python virtual environment

Go to the project directory and create a python virtual environment. You can use any name you want for the environment, here we will call it `crypto_env`:

`python -m venv crypto_env`

Activate the virtual environment:

`source crypto_env/bin/activate` or `crypto_env\Scripts\activate`

The actions can also be performed into a Terminal instead of an IDE, howver, you would need to start the command line as administrator.

From here the commands are executed using python package `pip`, so if you do not have it yet, make sure to install it first into your machine and adding python `bin` to your system environment variables under `PATH`. Follow the instructions here for more details: [Tutorial Python](https://realpython.com/add-python-to-path/).

#### 3. Enter current folder

Now, you should be in the correct directory already:

`cd ./Exercise_1`

#### 4. Install the dependencies
Automatically install all the required python packages:

`pip install -r requirements.txt`

#### 5. Run the project
Run the program by executing `cryptology.py`:

`python cryptology.py`

Enjoy!





