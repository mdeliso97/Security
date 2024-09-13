
#!/bin/bash

echo "Activating virtual environment..."
source crypto_env/bin/activate
echo "Activation complete."

echo "Start application..."
python3 cryptology.py
echo "Execution complete."
