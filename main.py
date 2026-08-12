"""
EngagePro Chatbot
=================

Execution Instructions
----------------------
1. Activate the project virtual environment.

2. Install the required dependencies (if not already installed):

       pip install -r requirements.txt

3. Launch the application:

       python main.py

This script starts the Streamlit user interface.
"""

import subprocess
import sys


def main():
    """Launch the Streamlit application."""
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "app.py"]
    )


if __name__ == "__main__":
    main()