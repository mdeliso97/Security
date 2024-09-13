# Crypto 8-bit

Welcome to the Crypto 8-bit project!

## What is Crypto 8-bit

Crypto 8-bit is a small utility program that guides and helps users to encrypt/decrypt files or folders by using some of the most used ciphers nowadays: ECB, CBC, GCM, RSA, and RSA OAEP. The program gives the user full choice of the encryption approach, namely Symmetric Encryption or Asymmetric Encryption.

## How to use Crypto 8-bit

#### Guide through the UI

TBD

#### Example use Case

TBD

#### Further Insights

TBD

## Instructions to getting started with the project

The Crypto 8-bit program has a main file called  ```cryptology.py```. The program, when started has an interactive GUI that allows Users to encrypt or decrypt by selecting their preferences between symmetric cipher and asymmetric cipher.

The ```codificator.py``` and ```RSA_Keygen.py``` are utility classes, the first one holds methods to decode or encode from string or integer to byte format by taking the text file as input, depending on the needs. The second class becomes fundamental for the asymmetric cipher to produce keys. If the User does not have a public and private key, he can through the ```keygen``` button in the GUI generate a pair.

The other classes, namely ```CBC.py```, ```ECB.py```, ```GCM.py```, ```RSA.py``` and ```RSA_OAEP.py``` define the different ciphers' logic.

Finally, ```installer_Windows.bat``` and ```installer_Linux.sh``` are scripts for the automatic installation of the program and its dependencies.

The symmetric key is randomized if the user does not provide any password, since in this program, the user is allowed to choose the encryption/decryption key.

It is recommended to use the auto installer for a soft installation, hence a local installation all-in-one in the folder.

## How to run the program

### Using auto installer (Windows + Linux)

#### 1. Import Project

Download the GitHub repository from [Repository](https://GitHub.com/mdeliso97/Security)

#### 2. Install program

To install the program you simply need on **Windows** to double-click the file ```installer_Windows.bat``` or execute the following 2 lines on Linux:

```chmod +x ./installer_Linux.sh```
```./installer_Linux.sh```

. This program will do all the installation (including Python version 3.9.13) for you and create a separate file called ```Crypto_8-bit.bat``` or ```Crypto_8-bit.sh```. In addition, obsolete folders and files used for installation will be automatically uninstalled.

#### 4. Run the program

To run the program, double-click on the file ```Crypto_8-bit.bat``` or ```Crypto_8-bit.sh```, if it does not work, open a terminal and navigate to your ```Crypto_8-bit.sh``` directory and run into your console:

`./Crypto_8-bit.sh`, in Linux system, if you have permission problems, run the following two lines:

```chmod +x ./Crypto_8-bit.sh```
```./Crypto_8-bit.sh```

Make sure to be in the same folder of the file. The double-click may not work sometimes in Linux machines due to default security measures or user preferences.

The program should start automatically.

### Manually run the program (Windows)

#### 0. Install Python the latest version

To install correctly this program, you will need to install Python 3.9.13 version or later, see [Python 3.9.13 for Windows](https://www.python.org/downloads/windows/), scroll down until you find the correct version compatible with your system.

For the direct download link, follow hereafter:

[Python 3.9.13 for macOS](https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg)

[Python 3.9.13 for Windows amd64 (64-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)

[Python 3.9.13 for Windows (32-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe)

As soon as you start the installer, make sure to check the checkbox ***Add python 3.9.13 to PATH***. To check whether the installation was successful, restart your system, open a terminal, and write `python --version`, if it outputs `python 3.9.13`, you successfully installed the version.

#### 1. Import Project

Download the GitHub repository from [Repository](https://GitHub.com/mdeliso97/Security)

#### 2. Create a Python virtual environment

Go to the project directory and create a Python virtual environment. You can use any name you want for the environment, here we will call it `crypto_env`:

`python -m venv crypto_env`

Activate the virtual environment:

`crypto_env\Scripts\activate`

The actions can also be performed in a Terminal instead of an IDE, however, you would need to start the command line as an administrator.

#### 3. Enter current folder

Now, you should be in the correct directory already:

`cd ./Crypto_8-bit`

#### 4. Install the dependencies
Automatically install all the required Python packages:

`pip install -r requirements.txt`

#### 5. Run the project
Run the program by executing `cryptology.py`:

`python cryptology.py`

### Manually run the program (Linux)

#### 0. Install Python the latest version

To install correctly this program, you will need to install Python 3.9.13 version or later, see [Python 3.9.13 for Windows](https://www.python.org/downloads/windows/), scroll down until you find the correct version compatible with your system.

For the direct download link, follow hereafter:

[Python 3.9.13 for macOS](https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg)

[Python 3.9.13 for Windows amd64 (64-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)

[Python 3.9.13 for Windows (32-bit)](https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe)

[Python 3.9.13 for Linux/Unix](https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz)

As soon as you start the installer, make sure to check the checkbox ***Add python 3.9.13 to PATH***. To check whether the installation was successful, restart your system, open a terminal, and write `python --version`, if it outputs `python 3.9.13`, you successfully installed the version.

#### 1. Import Project

Download the GitHub repository from [Repository](https://GitHub.com/mdeliso97/Security)

#### 2. Create a Python virtual environment

Go to the project directory and create a Python virtual environment. You can use any name you want for the environment, here we will call it `crypto_env`:

`python -m venv crypto_env`

Activate the virtual environment:

`source crypto_env/bin/activate`

The actions can also be performed in a Terminal instead of an IDE, however, you would need to start the command line as an administrator.

#### 3. Enter current folder

Now, you should be in the correct directory already:

`cd ./Crypto_8-bit`

#### 4. Install the dependencies
Automatically install all the required Python packages:

`pip install -r requirements.txt`

#### 5. Run the project
Run the program by executing `cryptology.py`:

`python cryptology.py`

Thank you for using the program and kindly leave comments or suggestions if you find any error or cool features to have!





