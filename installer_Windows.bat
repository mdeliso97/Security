@echo off

set parent_dir=%CD%

set python_version=3.9.13

set python_path="%parent_dir%/Utilities"

cd %python_path%

echo Extract the source code...

tar -xvf Python-%python_version%.tgz

echo configure, build, and install Python...

./configure --prefix=%python_path%

echo Install Python...

start /wait python-%python_version%-amd64.exe /quiet TargetDir=%python_path%

echo completed installation of Python %python_version%

echo clean up

cd %python_path%

rm -rf Python-%python_version%

rm Python-%python_version%.tgz

cd %parent_dir%



echo Initializing virtual environment...

python -m venv crypto_env

echo Complete

echo activating virtual environment...

call crypto_env\Scripts\activate.bat

:: Add the Python installation path to the PATH

set PATH=%python_path%;%PATH%

echo Activation complete

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