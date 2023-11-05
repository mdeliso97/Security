@echo off

set parent_dir=%CD%

set python_version=3.9.13

set python_path=%parent_dir%/Utilities

:: Start installation of the correct version of Python

cd %python_path%

echo Install Python...

python-%python_version%-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo completed installation of Python %python_version%

echo clean up

rm /q python-%python_version%-amd64.exe

rmdir /s /q Python-%python_version%.tgz

cd %parent_dir%

:: Start installation of the working environment

echo Initializing virtual environment...

python -m venv crypto_env

echo Complete

echo activating virtual environment...

call crypto_env\Scripts\activate.bat

:: Add the Python installation path to the PATH

set PATH=%python_path%;%PATH%

echo Activation complete

:: Add all dependencies to the virtual environment

echo install dependencies...

pip install -r requirements.txt

echo complete

:: Create a new batch file for running the application

(
  echo @echo off
  echo echo Activating virtual environment...
  echo call crypto_env\Scripts\activate.bat
  echo echo Activation complete.
  echo echo Start application...
  echo python cryptology.py
  echo echo Execution complete.
) > Crypto_8-bit.bat