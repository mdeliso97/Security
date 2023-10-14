# Crypto 8-bit

Welcome to Crypto 8-bit project, a cryptology project 

## Instructions to getting started with the project

The Crypto 8-bit program has a main file which is called  ```cryptology.py```. The program, when started has an interactive GUI which allows Users to encrypt or decrypt by selecting their preferences between symmetric cipher and asymmetric cipher.

The ```codificator.py``` and ```RSA_Keygen.py``` are utility classes, the first one holds methods to decode or encode from string or integer to byte format by taking the text file as input, depending on the needs. The second class becomes fundamental for the asymmetric cipher to produce keys. If the User does not have a public and private key, he can through the ```keygen``` button in the GUI generate a pair.

The other classes, namely ```CBC.py```, ```ECB.py```, ```GCM.py```, ```RSA.py``` and ```RSA_OAEP.py``` define the different ciphers' logic.

The symmetric key is randomized if the user does not provide any password, since in this program, the user is allowed to choose the encryption/decryption key.

## How to run the program

#### 1. Import Project

Download the GitHub repository from GitHub.com

#### 2. Create a Python virtual environment

Go to the project directory and create a python virtual environment. You can use any name you want for the environment, here we will call it `crypto_env`:

`python -m venv crypto_env`

Activate the virtual environment:

`source crypto_env/bin/activate` or `crypto_env\Scripts\activate`

The actions can also be performed into a Terminal instead of an IDE, however, you would need to start the command line as administrator.

From here the commands are executed using python package `pip`, so if you do not have it yet, make sure to install it first into your machine and adding python `bin` to your system environment variables under `PATH`. Follow the instructions here for more details: [Tutorial Python](https://realpython.com/add-python-to-path/).

#### 3. Enter current folder

Now, you should be in the correct directory already:

`cd ./Crypto_8-bit`

#### 4. Install the dependencies
Automatically install all the required python packages:

`pip install -r requirements.txt`

#### 5. Run the project
Run the program by executing `cryptology.py`:

`python cryptology.py`

Enjoy!





