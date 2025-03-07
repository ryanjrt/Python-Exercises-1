# setup.sh
#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Notify user
echo "Environment setup complete. Dependencies are installed."
