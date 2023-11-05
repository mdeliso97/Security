@echo off

parent_dir="$(pwd)"

python_version="3.9.13"

python_path="$parent_dir/Utilities"

cd Utilities/Python-$python_version

echo Extract the source code...

tar -xvf Python-$python_version.tgz

echo Configure, build, and install Python

./configure --prefix=$python_path

make

sudo make install

echo completed installation of Python $python_version

echo clean up

cd ..

rm -rf Python-$python_version

rm Python-$python_version.tgz

cd $parent_dir



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
  echo export PATH="$python_path:$PATH"
  echo echo Activation complete.
  echo echo Start application...
  echo python cryptology.py
  echo echo Execution complete.
) > Crypto_8-bit.bat