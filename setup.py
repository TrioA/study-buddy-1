# ==========================================
# StudyBuddy Chatbot
# Setup Script
# ==========================================

"""
StudyBuddy Setup Script

Checks for required dependencies and installs any missing ones.
Also offers to create a shortcut/alias for convenient launching.
"""

import subprocess
import sys
import os


REQUIRED_PACKAGES = [
    # tkinter is part of Python standard library on Windows
    # No external packages required for basic functionality
]

# These are standard library modules we need
REQUIRED_STDLIB = [
    "tkinter",      # For GUI mode
    "json",         # For user data persistence
    "random",       # For random selections
    "re",           # For regex matching
    "time",         # For typing effect delays
    "threading",    # For background processing in GUI
    "pathlib",      # For file path handling
    "datetime",     # For timestamps
    "difflib",      # For spell correction
    "textwrap",     # For text wrapping
    "math",         # For maths calculations
    "statistics",   # For statistical operations
]


def check_python_version():
    """Check if Python version is sufficient."""
    required_version = (3, 7)
    current_version = sys.version_info[:2]

    if current_version < required_version:
        print(f"❌ Python {required_version[0]}.{required_version[1]}+ is required.")
        print(f"   You have Python {current_version[0]}.{current_version[1]}.")
        print("   Please upgrade Python from https://www.python.org/downloads/")
        return False

    print(f"✅ Python {current_version[0]}.{current_version[1]} detected")
    return True


def check_tkinter():
    """Check if tkinter is available (needed for GUI mode)."""
    try:
        import tkinter
        print(f"✅ tkinter {tkinter.TkVersion} detected (GUI mode available)")
        return True
    except ImportError:
        print("⚠️  tkinter not found (GUI mode unavailable)")
        print("   tkinter is included with Python on Windows.")
        print("   If missing, reinstall Python and ensure 'tcl/tk' is checked.")
        return False


def install_packages():
    """Install any missing packages."""
    if not REQUIRED_PACKAGES:
        print("✅ No external packages required.")
        return True

    for package in REQUIRED_PACKAGES:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(f"✅ Installed: {package}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install: {package}")
            return False

    return True


def main():
    """Run the setup checks."""
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("=" * 50)
    print("StudyBuddy - Setup")
    print("=" * 50)
    print()

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    print()

    # Check tkinter
    gui_available = check_tkinter()

    print()

    # Install packages
    install_packages()

    print()
    print("=" * 50)
    print("✅ Setup complete!")
    print()
    print("   Run the chatbot:")
    print("     python main.py          # Terminal (CLI) mode")
    print("     python main.py --gui    # GUI mode (floating window)")
    print()
    print("   Or use the --cli flag to force terminal mode.")
    print("   On first run, the app will ask you to pick your preference.")
    print("=" * 50)


if __name__ == "__main__":
    main()