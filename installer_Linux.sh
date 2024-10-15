#!/bin/bash

parent_dir="$(pwd)"

python_version="3.9.13"

python_path="$parent_dir/Utilities"

sudo apt install python3-pip -y

cd $python_path

echo "extract the source code..."

tar -xvf Python-$python_version.tgz

echo "configure, build, and install Python"

cd "$python_path/Python-$python_version"

./configure --prefix="$python_path"

make

sudo make install

echo "completed installation of Python $python_version"

echo "clean up..."

cd $python_path

sudo rm -rf Python-$python_version

rm -f Python-$python_version.tgz

rm python-$python_version-amd64.exe

cd $parent_dir

echo "Initializing virtual environment..."

# Check if virtual environment already exists
if [ ! -d "crypto_env" ]; then
    python3 -m venv crypto_env
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

echo "Complete"

echo "Activating virtual environment..."

. crypto_env/bin/activate

if [ $? -eq 0 ]; then
    echo "Virtual environment activated successfully."
else
    echo "Failed to activate the virtual environment."
    exit 1
fi

echo "Installing dependencies..."

pip install python3-tk  # No -y option for pip
pip install -r requirements.txt

echo "Dependencies installed."

# Create a new shell script
echo "Creating Crypto_8-bit.sh..."

cat <<EOL > Crypto_8-bit.sh
#!/bin/bash

echo "Activating virtual environment..."
. crypto_env/bin/activate

if [ $? -eq 0 ]; then
    echo "Virtual environment activated successfully."
else
    echo "Failed to activate the virtual environment."
    exit 1
fi

echo "Starting application..."
python cryptology.py
echo "Application execution complete."
EOL

chmod +x Crypto_8-bit.sh
