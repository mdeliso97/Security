#!/bin/bash

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