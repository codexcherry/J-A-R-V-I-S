#!/usr/bin/env python3
"""
JARVIS AI Assistant - Main Entry Point
This script provides a safe way to run JARVIS with proper error handling.
"""

import sys
import os
import traceback
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed."""
    required_modules = [
        'PyQt5', 'cohere', 'groq', 'huggingface_hub', 
        'selenium', 'edge_tts', 'pygame', 'requests'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        print("❌ Missing required dependencies:")
        for module in missing_modules:
            print(f"   - {module}")
        print("\nPlease run: python setup.py")
        return False
    
    return True

def check_config():
    """Check if configuration is properly set up."""
    try:
        import config
        if not config.validate_api_keys():
            return False
        return True
    except ImportError:
        print("❌ Configuration file not found!")
        print("Please create config.py with your API keys.")
        return False
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def check_directories():
    """Check if required directories exist."""
    required_dirs = [
        "Backend/Data",
        "Frontend/Files", 
        "Data",
        "Temp/Files"
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
    
    if missing_dirs:
        print("❌ Missing required directories:")
        for dir_path in missing_dirs:
            print(f"   - {dir_path}")
        print("\nPlease run: python setup.py")
        return False
    
    return True

def main():
    """Main entry point with comprehensive error handling."""
    print("🤖 JARVIS AI Assistant")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Check dependencies
    print("🔍 Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("✓ All dependencies installed")
    
    # Check configuration
    print("🔍 Checking configuration...")
    if not check_config():
        sys.exit(1)
    print("✓ Configuration valid")
    
    # Check directories
    print("🔍 Checking directories...")
    if not check_directories():
        sys.exit(1)
    print("✓ All directories exist")
    
    # Add project root to Python path
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))
    
    try:
        print("🚀 Starting JARVIS...")
        from Frontend.Main import main as jarvis_main
        jarvis_main()
    except KeyboardInterrupt:
        print("\n👋 JARVIS stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        print("\nFull error details:")
        traceback.print_exc()
        print("\nPlease check the error above and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
