# Crypto 8-bit

Welcome to Crypto 8-bit project, a cryptology project 

## Instructions to getting started with the project

The Crypto 8-bit program has a main file which is called  ```cryptology.py```. The program, when started has an interactive GUI which allows Users to encrypt or decrypt by selecting their preferences between symmetric cipher and asymmetric cipher.

The ```codificator.py``` and ```RSA_Keygen.py``` are utility classes, the first one holds methods to decode or encode from string or integer to byte format by taking the text file as input, depending on the needs. The second class becomes fundamental for the asymmetric cipher to produce keys. If the User does not have a public and private key, he can through the ```keygen``` button in the GUI generate a pair.

The other classes, namely ```CBC.py```, ```ECB.py```, ```GCM.py```, ```RSA.py``` and ```RSA_OAEP.py``` define the different ciphers' logic.

Finally, ```installer_Windows.bat``` and ```installer_Linux.sh``` are scripts for the automatic installation of the program and its dependencies.

The symmetric key is randomized if the user does not provide any password, since in this program, the user is allowed to choose the encryption/decryption key.

## How to run the program

### Using auto installer (Windows + Linux)

#### 0. Install python the latest version

To install correctly this program, you will need to install python 3.9.13 version or later, see [Python 3.9.13 for Windows](https://www.python.org/downloads/windows/), scroll down until you find the correct version compatible with your system.

For direct installation link, follow hereafter:

[Python 3.9.13 for macOS](https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg)

[Python 3.9.13 for Windows amd64 (64-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)

[Python 3.9.13 for Windows (32-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe)

As soon as you start the installer, make sure to check the checkbox ***Add python 3.9.13 to PATH***. To check whether the installation was successfully, restart your system, open a terminal and write `python --version`, if it outputs `python 3.9.13`, you successfully installed the version.

#### 1. Import Project

Download the GitHub repository from [Repository](https://GitHub.com/mdeliso97/Security)

#### 2. Install program

To install the program it is simply needed to double-click on the file ```installer_Windows.bat``` or ```installer_Linux.sh```. This program will do all the installation for you and create a separated file called ```Crypto_8-bit.bat``` or ```Crypto_8-bit.sh```.

#### 3. Run the program

To run the program, double-click on the file ```Crypto_8-bit.bat``` or open a terminal and navigate to your ```Crypto_8-bit.sh``` directory and run into your console:

`./Crypto_8-bit.sh`. The double-click may not work sometimes in Linux machines due to default security measures or user preferences.

The program should start automatically.

### Manually run the program (Windows)

#### 0. Install python the latest version

To install correctly this program, you will need to install python 3.9.13 version or later, see [Python 3.9.13 for Windows](https://www.python.org/downloads/windows/), scroll down until you find the correct version compatible with your system.

For direct installation link, follow hereafter:

[Python 3.9.13 for macOS](https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg)

[Python 3.9.13 for Windows amd64 (64-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)

[Python 3.9.13 for Windows (32-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe)

As soon as you start the installer, make sure to check the checkbox ***Add python 3.9.13 to PATH***. To check whether the installation was successfully, restart your system, open a terminal and write `python --version`, if it outputs `python 3.9.13`, you successfully installed the version.

#### 1. Import Project

Download the GitHub repository from [Repository](https://GitHub.com/mdeliso97/Security)

#### 2. Create a Python virtual environment

Go to the project directory and create a python virtual environment. You can use any name you want for the environment, here we will call it `crypto_env`:

`python -m venv crypto_env`

Activate the virtual environment:

`crypto_env\Scripts\activate`

The actions can also be performed into a Terminal instead of an IDE, however, you would need to start the command line as administrator.

#### 3. Enter current folder

Now, you should be in the correct directory already:

`cd ./Crypto_8-bit`

#### 4. Install the dependencies
Automatically install all the required python packages:

`pip install -r requirements.txt`

#### 5. Run the project
Run the program by executing `cryptology.py`:

`python cryptology.py`

### Manually run the program (Linux)

#### 0. Install python the latest version

To install correctly this program, you will need to install python 3.9.13 version or later, see [Python 3.9.13 for Windows](https://www.python.org/downloads/windows/), scroll down until you find the correct version compatible with your system.

For direct installation link, follow hereafter:

[Python 3.9.13 for macOS](https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg)

[Python 3.9.13 for Windows amd64 (64-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)

[Python 3.9.13 for Windows (32-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe)

[Python 3.9.13 for Linux/Unix](https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz)

As soon as you start the installer, make sure to check the checkbox ***Add python 3.9.13 to PATH***. To check whether the installation was successfully, restart your system, open a terminal and write `python --version`, if it outputs `python 3.9.13`, you successfully installed the version.

#### 1. Import Project

Download the GitHub repository from [Repository](https://GitHub.com/mdeliso97/Security)

#### 2. Create a Python virtual environment

Go to the project directory and create a python virtual environment. You can use any name you want for the environment, here we will call it `crypto_env`:

`python -m venv crypto_env`

Activate the virtual environment:

`source crypto_env/bin/activate`

The actions can also be performed into a Terminal instead of an IDE, however, you would need to start the command line as administrator.

#### 3. Enter current folder

Now, you should be in the correct directory already:

`cd ./Crypto_8-bit`

#### 4. Install the dependencies
Automatically install all the required python packages:

`pip install -r requirements.txt`

#### 5. Run the project
Run the program by executing `cryptology.py`:

`python cryptology.py`

Thank you for using the program and kindly leave comments or suggestions if you find any error or cool features to have!





