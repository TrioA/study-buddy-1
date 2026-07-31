# ==========================================
# StudyBuddy Chatbot
# Main Program
# Version 3.0
# ==========================================

"""
StudyBuddy Chatbot

Main entry point of the project.
Choose between CLI mode or GUI mode.
Preferences can be saved to avoid asking every time.

Developed by:
Amoli Agrawal (Class 9)
Arav Gupta (Class 10)
"""

import sys
import json
import os
from pathlib import Path


CONFIG_FILE = Path("studybuddy_config.json")


def load_config():
    """Load the saved configuration."""
    if not CONFIG_FILE.exists():
        return {}
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_config(config):
    """Save the configuration."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


def prompt_mode_selection():
    """Ask the user which mode they want."""
    print("\n" + "=" * 50)
    print("📚  StudyBuddy - Select Mode")
    print("=" * 50)
    print()
    print("How would you like to interact with StudyBuddy?")
    print()
    print("  1) GUI mode (floating window with dark theme)")
    print("  2) CLI mode (terminal / command line)")
    print()

    while True:
        choice = input("Your choice (1 or 2): ").strip()
        if choice == "1":
            return "gui"
        elif choice == "2":
            return "cli"
        print("  Please enter 1 for GUI or 2 for CLI.")


def prompt_remember_preference(mode):
    """Ask if the user wants to remember their preference."""
    print()
    while True:
        choice = input(f"Remember this preference ({mode}) for next time? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        print("  Please enter y or n.")


def prompt_preference_conflict(saved_mode, requested_mode):
    """Ask the user how to handle a mode mismatch."""
    print()
    print("=" * 50)
    print("⚠️  Mode Mismatch")
    print("=" * 50)
    print()
    print(f"  Saved preference : {saved_mode.upper()}")
    print(f"  Requested flag   : --{requested_mode}")
    print()
    print("  What would you like to do?")
    print()
    print("  1) Update saved preference to match this flag")
    print("  2) Remove saved preference (ask every time)")
    print("  3) Use this mode once (don't change saved preference)")
    print()

    while True:
        choice = input("Your choice (1, 2, or 3): ").strip()
        if choice == "1":
            return "update"
        elif choice == "2":
            return "remove"
        elif choice == "3":
            return "once"
        print("  Please enter 1, 2, or 3.")


def run_setup():
    """Run setup checks before starting."""
    try:
        print("🔍 Running setup checks...")
        import subprocess
        result = subprocess.run(
            [sys.executable, "setup.py"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ Setup checks passed.")
        else:
            print("⚠️  Setup checks had issues, but continuing...")
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
    except Exception as e:
        print(f"⚠️  Setup check warning: {e}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    # Run setup checks
    run_setup()

    config = load_config()
    saved_mode = config.get("mode")

    # Detect flags
    has_gui_flag = "--gui" in sys.argv
    has_cli_flag = "--cli" in sys.argv

    # If both flags or no flags, determine mode
    if has_gui_flag and has_cli_flag:
        print("⚠️  Both --gui and --cli specified. Defaulting to CLI.")
        mode = "cli"
    elif has_gui_flag:
        if saved_mode and saved_mode != "gui":
            # Conflict: saved preference doesn't match flag
            action = prompt_preference_conflict(saved_mode, "gui")
            if action == "update":
                save_config({"mode": "gui"})
                print("✅ Preference updated to GUI.")
            elif action == "remove":
                CONFIG_FILE.unlink(missing_ok=True)
                print("✅ Preference removed. You will be asked next time.")
            # action == "once": keep saved preference unchanged
        elif not saved_mode:
            # No saved preference - ask if they want to save it
            if prompt_remember_preference("gui"):
                save_config({"mode": "gui"})
                print("✅ Preference saved as GUI.")
        mode = "gui"
    elif has_cli_flag:
        if saved_mode and saved_mode != "cli":
            action = prompt_preference_conflict(saved_mode, "cli")
            if action == "update":
                save_config({"mode": "cli"})
                print("✅ Preference updated to CLI.")
            elif action == "remove":
                CONFIG_FILE.unlink(missing_ok=True)
                print("✅ Preference removed. You will be asked next time.")
        elif not saved_mode:
            if prompt_remember_preference("cli"):
                save_config({"mode": "cli"})
                print("✅ Preference saved as CLI.")
        mode = "cli"
    else:
        # No flags - use saved preference or prompt
        if saved_mode:
            mode = saved_mode
            print(f"📌 Using saved preference: {mode.upper()} mode")
        else:
            mode = prompt_mode_selection()
            if prompt_remember_preference(mode):
                save_config({"mode": mode})
                print(f"✅ Preference saved as {mode.upper()}.")

    print()

    # Launch the selected mode
    if mode == "gui":
        try:
            try:
                from .gui import main as gui_main
            except ImportError:
                from gui import main as gui_main
            gui_main()
        except ImportError as e:
            print(f"❌ GUI mode unavailable: {e}")
            print("   Falling back to CLI mode.\n")
            try:
                from .chatbot import start_chatbot
            except ImportError:
                from chatbot import start_chatbot
            start_chatbot()
    else:
        try:
            from .chatbot import start_chatbot
        except ImportError:
            from chatbot import start_chatbot
        start_chatbot()


if __name__ == "__main__":
    main()