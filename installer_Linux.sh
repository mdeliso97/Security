#!/bin/bash

parent_dir="$(pwd)"

python_version="3.9.13"

# Directory where Python will be installed
python_path="$parent_dir/Utilities"

# Ensure pip is installed
sudo apt install python3-pip -y

cd $python_path

# Extract Python source code
echo "Extracting the source code..."
tar -xvf Python-$python_version.tgz

# Configure, build, and install Python
echo "Configuring, building, and installing Python $python_version"
cd "$python_path/Python-$python_version"

# Reconfigure the build with the proper OpenSSL path
./configure --prefix="$python_path" --with-openssl=/usr/include/openssl
make
sudo make install

# Ensure new Python binary is used
new_python_bin="$python_path/bin/python3.9"

# Verify the installation
if [ ! -f "$new_python_bin" ]; then
    echo "Python $python_version installation failed."
    exit 1
else
    echo "Python $python_version installed successfully."
fi

# Clean up the source code directory and tarball
echo "Cleaning up..."
cd $python_path
sudo rm -rf Python-$python_version
rm -f Python-$python_version.tgz
rm -f python-$python_version-amd64.exe

# Return to the parent directory
cd $parent_dir

echo "Initializing virtual environment..."

# Check if virtual environment already exists
if [ ! -d "crypto_env" ]; then
    # Use the newly installed Python binary to create the virtual environment
    $new_python_bin -m venv crypto_env
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

echo "Complete"

echo "Activating virtual environment..."

# Activate the virtual environment
if [ -f "crypto_env/bin/activate" ]; then
    . crypto_env/bin/activate
else
    echo "Failed to find activate script in crypto_env/bin/"
    exit 1
fi

# Check if activation succeeded
if [ $? -eq 0 ]; then
    echo "Virtual environment activated successfully."
else
    echo "Failed to activate the virtual environment."
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
pip install python3-tk
pip install -r requirements.txt

echo "Dependencies installed."

# Create a new shell script for the crypto app
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

# Make the script executable
chmod +x Crypto_8-bit.sh