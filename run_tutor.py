#!/usr/bin/env python3
"""
AI Tutor Chatbot Launcher
This script helps you easily start the AI tutor application.
"""

import os
import sys
import subprocess
import importlib

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'matplotlib', 'plotly', 
        'scikit-learn', 'nltk', 'textblob', 'sympy'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def install_dependencies():
    """Install missing dependencies"""
    print("Installing required packages...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True, text=True)
        print("✅ All dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        print(f"Error output: {e.stderr}")
        return False

def download_nltk_data():
    """Download required NLTK data"""
    print("Downloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('vader_lexicon', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✅ NLTK data downloaded successfully!")
    except Exception as e:
        print(f"⚠️  Warning: Could not download NLTK data: {e}")
        print("The application will still work, but some NLP features might be limited.")

def run_application():
    """Launch the Streamlit application"""
    print("🚀 Starting AI Tutor Chatbot...")
    print("📖 The application will open in your default web browser.")
    print("💡 If it doesn't open automatically, go to: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the application\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running the application: {e}")
        return False
    except KeyboardInterrupt:
        print("\n👋 Thanks for using AI Tutor Chatbot!")
        return True

def main():
    """Main launcher function"""
    print("🎓 AI Tutor Chatbot Launcher")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("app.py"):
        print("❌ Error: app.py not found in current directory")
        print("Please make sure you're running this script from the AI tutor directory.")
        return
    
    # Check dependencies
    missing_deps = check_dependencies()
    
    if missing_deps:
        print(f"📦 Missing packages: {', '.join(missing_deps)}")
        install_choice = input("Install missing packages? (y/n): ").lower().strip()
        
        if install_choice in ['y', 'yes']:
            if not install_dependencies():
                print("❌ Failed to install dependencies. Please install manually:")
                print("pip install -r requirements.txt")
                return
        else:
            print("❌ Cannot run without required packages.")
            return
    else:
        print("✅ All dependencies are installed!")
    
    # Download NLTK data
    download_nltk_data()
    
    # Run the application
    print("\n" + "=" * 40)
    run_application()

if __name__ == "__main__":
    main()
