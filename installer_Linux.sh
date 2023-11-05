#!/bin/bash

parent_dir="$(pwd)"

python_version="3.9.13"

python_path="$parent_dir/Utilities"

cd $python_path

echo "extract the source code..."

tar -xvf Python-$python_version.tgz

echo "configure, build, and install Python"

./configure --prefix=$python_path

make

sudo make install

echo "completed installation of Python $python_version"

echo "clean up..."

cd $python_path

rm -rf Python-$python_version

rm -f Python-$python_version.tgz

rm python-$python_version-amd64.exe

cd $parent_dir

echo "Initializing virtual environment..."

python -m venv crypto_env

echo "Complete"

echo "Activating virtual environment..."

source crypto_env/bin/activate

echo "Complete"

echo "Installing dependencies..."

pip install -r requirements.txt

echo "Complete"

# Create a new shell script

cat <<EOL > Crypto_8-bit.sh

#!/bin/bash

echo "Activating virtual environment..."
source crypto_env/bin/activate
echo "Activation complete."

echo "Start application..."
python cryptology.py
echo "Execution complete."
EOL

chmod +x Crypto_8-bit.sh