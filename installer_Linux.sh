#!/bin/bash

parent_dir="$(pwd)"

python_version="3.9.13"

python_path="$parent_dir/Utilities"

cd $python_path

echo "extract the source code..."

tar -xvf Python-$python_version.tgz

echo "configure, build, and install Python"

cd "$python_path/Python-$python_version"

./configure --prefix="$python_path"

make

make install

echo "completed installation of Python $python_version"

echo "clean up..."

cd $python_path

rm -rf Python-$python_version

rm -f Python-$python_version.tgz

rm python-$python_version-amd64.exe

new_python_bin="$python_path/bin/python3.9"

cd $parent_dir

echo "Initializing virtual environment..."

$new_python_bin -m venv crypto_env

echo "Complete"

echo "Activating virtual environment..."

. crypto_env/bin/activate

echo "Complete"

echo "Installing dependencies..."

apt install python3-pip -y

apt install python3-tk -y

pip install -r requirements.txt

echo "Complete"

# Create a new shell script

cat <<EOL > Crypto_8-bit.sh

#!/bin/bash

echo "Activating virtual environment..."
. crypto_env/bin/activate
echo "Activation complete."

echo "Start application..."
python3 cryptology.py
echo "Execution complete."
EOL

chmod +x Crypto_8-bit.sh