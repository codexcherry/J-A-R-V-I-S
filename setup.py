#!/usr/bin/env python3
"""
Simple setup script for JARVIS AI Assistant
Creates necessary directories and installs dependencies.
"""

import os
import subprocess
import sys
from pathlib import Path

def create_directories():
    """Create necessary directories for JARVIS."""
    directories = [
        "Backend/Data",
        "Frontend/Files",
        "Data",
        "Temp/Files"
    ]
    
    print("📁 Creating directories...")
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {directory}")

def install_dependencies():
    """Install required dependencies."""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True, text=True)
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        print("Please run manually: pip install -r requirements.txt")
        return False

def main():
    """Main setup function."""
    print("🤖 JARVIS AI Assistant Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Create directories
    create_directories()
    
    # Install dependencies
    install_dependencies()
    
    print("\n🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Edit config.py with your API keys")
    print("2. Run: python app.py")

if __name__ == "__main__":
    main()