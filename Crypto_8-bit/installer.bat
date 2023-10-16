@echo off

echo Initializing virtual environment...

python -m venv crypto_env

echo Complete

echo activating virtual environment...

call crypto_env\Scripts\activate.bat

echo complete

echo install dependencies...

pip install -r requirements.txt

echo complete

REM Create a new batch file
(
  echo @echo off
  echo echo Activating virtual environment...
  echo call crypto_env\Scripts\activate.bat
  echo echo Activation complete.
  echo echo Start application...
  echo python cryptology.py
  echo echo Execution complete.
) > Crypto_8-bit.bat