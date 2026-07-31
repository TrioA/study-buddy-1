# ==========================================
# StudyBuddy Chatbot - GUI
# gui.py
# ==========================================

import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
import random

try:
    from .chatbot import (
        load_user, save_user, update_history,
        correct_input, detect_intents, build_reply,
        should_exit, WELCOME_MESSAGE, GOODBYE_QUOTES,
        ERROR_MESSAGES, BOT_NAME, get_user_instructions
    )
except ImportError:
    from chatbot import (
        load_user, save_user, update_history,
        correct_input, detect_intents, build_reply,
        should_exit, WELCOME_MESSAGE, GOODBYE_QUOTES,
        ERROR_MESSAGES, BOT_NAME, get_user_instructions
    )

# -----------------------------
# GUI Chatbot
# -----------------------------

class StudyBuddyGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("StudyBuddy")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        # Window dimensions
        self.WINDOW_WIDTH = 420
        self.WINDOW_HEIGHT = 560

        # Position - bottom right corner
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = screen_width - self.WINDOW_WIDTH - 20
        y = screen_height - self.WINDOW_HEIGHT - 60
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{x}+{y}")

        # Make window stay on top
        self.root.attributes("-topmost", True)

        # Colors
        self.bg_color = "#1e1e2e"
        self.fg_color = "#cdd6f4"
        self.accent_color = "#89b4fa"
        self.user_bubble = "#45475a"
        self.bot_bubble = "#313244"
        self.input_bg = "#313244"
        self.send_btn_color = "#89b4fa"

        # Typing state
        self.typing_active = False
        self.typing_queue = []
        self.typing_speed = 0.02

        # User data
        self.user = load_user()

        # Build UI
        self._build_ui()

        # Show welcome
        self.root.after(500, self._show_welcome)

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _build_ui(self):
        """Build the GUI components."""

        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color, height=50)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)

        header_label = tk.Label(
            header_frame,
            text="📚  StudyBuddy",
            font=("Segoe UI", 14, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        header_label.pack(side=tk.LEFT, padx=15, pady=10)

        # Separator
        sep = ttk.Separator(self.root, orient=tk.HORIZONTAL)
        sep.pack(fill=tk.X, padx=0)

        # Chat display area
        self.chat_frame = tk.Frame(self.root, bg=self.bg_color)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 0))

        self.chat_display = tk.Text(
            self.chat_frame,
            wrap=tk.WORD,
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg=self.fg_color,
            bd=0,
            highlightthickness=0,
            padx=10,
            pady=10,
            state=tk.DISABLED,
            cursor="arrow"
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.chat_display, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_display.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.chat_display.yview)

        # Configure text tags for styling
        self.chat_display.tag_config(
            "user_label",
            foreground="#a6e3a1",
            font=("Segoe UI", 9, "bold"),
            spacing1=8,
            spacing3=2
        )
        self.chat_display.tag_config(
            "user_msg",
            foreground=self.fg_color,
            font=("Segoe UI", 10),
            spacing1=0,
            spacing3=4,
            lmargin1=20
        )
        self.chat_display.tag_config(
            "bot_label",
            foreground=self.accent_color,
            font=("Segoe UI", 9, "bold"),
            spacing1=8,
            spacing3=2
        )
        self.chat_display.tag_config(
            "bot_msg",
            foreground=self.fg_color,
            font=("Segoe UI", 10),
            spacing1=0,
            spacing3=4,
            lmargin1=20
        )
        self.chat_display.tag_config(
            "typing_tag",
            foreground="#f5c2e7",
            font=("Segoe UI", 9, "italic"),
            spacing1=8,
            spacing3=4
        )
        self.chat_display.tag_config(
            "separator",
            foreground="#585b70",
            font=("Segoe UI", 6),
            spacing1=2,
            spacing3=2
        )

        # Input area
        input_frame = tk.Frame(self.root, bg=self.bg_color, height=60)
        input_frame.pack(fill=tk.X, padx=10, pady=(5, 10))
        input_frame.pack_propagate(False)

        # Input field
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            input_frame,
            textvariable=self.input_var,
            font=("Segoe UI", 10),
            bg=self.input_bg,
            fg=self.fg_color,
            bd=0,
            highlightthickness=1,
            highlightbackground="#45475a",
            highlightcolor=self.accent_color,
            insertbackground=self.fg_color,
            relief=tk.FLAT
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8), ipady=8)
        self.input_entry.bind("<Return>", self._on_send)
        self.input_entry.focus_set()

        # Stop button
        self.stop_btn = tk.Button(
            input_frame,
            text="Stop",
            font=("Segoe UI", 9, "bold"),
            bg="#f38ba8",
            fg="#1e1e2e",
            bd=0,
            padx=12,
            pady=6,
            cursor="hand2",
            activebackground="#eba0ac",
            activeforeground="#1e1e2e",
            command=self._on_stop
        )
        self.stop_btn.pack(side=tk.RIGHT, padx=(0, 6))

        # Send button
        self.send_btn = tk.Button(
            input_frame,
            text="Send",
            font=("Segoe UI", 9, "bold"),
            bg=self.send_btn_color,
            fg="#1e1e2e",
            bd=0,
            padx=15,
            pady=6,
            cursor="hand2",
            activebackground="#74c7ec",
            activeforeground="#1e1e2e",
            command=self._on_send
        )
        self.send_btn.pack(side=tk.RIGHT)

    def _add_text(self, text, tag):
        """Add text to the chat display."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, text + "\n", tag)
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def _add_separator(self):
        """Add a thin separator line."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, "─" * 50 + "\n", "separator")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def _type_text_async(self, text, tag, callback=None):
        """Type text character by character without blocking the GUI."""
        self.typing_active = True
        self.current_typing_text = text
        self.current_typing_tag = tag
        self.current_typing_callback = callback
        self._type_char(0, text, tag, callback)

    def _on_stop(self):
        """Finish typing response immediately when Stop button is clicked."""
        if not self.typing_active:
            return

        self.typing_active = False
        # Insert remainder of line immediately
        if hasattr(self, "current_typing_text") and self.current_typing_text:
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, self.current_typing_text[getattr(self, "_last_char_idx", 0):] + "\n", self.current_typing_tag)
            self.chat_display.see(tk.END)
            self.chat_display.config(state=tk.DISABLED)

        callback = getattr(self, "current_typing_callback", None)
        if callback:
            callback()

    def _type_char(self, index, text, tag, callback):
        """Type a single character and schedule the next one."""
        self._last_char_idx = index
        if not self.typing_active:
            return

        if index >= len(text):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, "\n", tag)
            self.chat_display.see(tk.END)
            self.chat_display.config(state=tk.DISABLED)
            self.typing_active = False
            if callback:
                callback()
            return

        char = text[index]
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, char, tag)
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

        delay = int(self.typing_speed * 1000)
        self.root.after(delay, lambda: self._type_char(index + 1, text, tag, callback))

    def _show_welcome(self):
        """Display the welcome message with typing effect."""
        self._add_text("🤖 StudyBuddy:", "bot_label")
        welcome_lines = list(WELCOME_MESSAGE)

        if self.user.get("first_run", True):
            instructions = get_user_instructions()
            if instructions:
                welcome_lines.append("")
                welcome_lines.extend(instructions)
            self.user["first_run"] = False
            save_user(self.user)

        self._type_lines_sequentially(welcome_lines, 0, lambda: self._add_text("", "separator"))

    def _on_send(self, event=None):
        """Handle send button click or Enter key."""
        user_text = self.input_var.get().strip()
        if not user_text:
            return

        if self.typing_active:
            return

        self.input_var.set("")
        self.input_entry.config(state=tk.DISABLED)
        self.send_btn.config(state=tk.DISABLED)

        # Show user message
        self._add_text("", "separator")
        self._add_text("👤 You:", "user_label")
        self._add_text(user_text, "user_msg")

        # Process in background thread
        threading.Thread(
            target=self._process_message,
            args=(user_text,),
            daemon=True
        ).start()

    def _process_message(self, user_text):
        """Process the user message in a background thread."""
        # Update history
        update_history(self.user, user_text)

        # Detect intent
        clean_text = correct_input(user_text)
        intents = detect_intents(clean_text)

        # Build reply
        reply = build_reply(self.user, intents, clean_text)

        # Check for exit
        exit_chat = should_exit(intents)

        # Save user data
        save_user(self.user)

        # Schedule reply display on main thread
        self.root.after(0, lambda: self._display_reply(reply, exit_chat))

    def _display_reply(self, reply, exit_chat):
        """Display the bot reply with typing effect."""
        self._add_text("🤖 StudyBuddy:", "bot_label")

        # Split multi-line replies and type each line
        lines = reply.split("\n")
        self._type_lines_sequentially(lines, 0, lambda: self._after_reply(exit_chat))

    def _type_lines_sequentially(self, lines, index, callback):
        """Type multiple lines one after another."""
        if index >= len(lines):
            if callback:
                callback()
            return

        line = lines[index]
        self._type_text_async(
            line,
            "bot_msg",
            callback=lambda: self._schedule_next_line(lines, index + 1, callback)
        )

    def _schedule_next_line(self, lines, next_index, callback):
        """Schedule the next line to be typed."""
        if next_index < len(lines):
            self.root.after(100, lambda: self._type_lines_sequentially(lines, next_index, callback))
        else:
            if callback:
                callback()

    def _after_reply(self, exit_chat):
        """Actions after reply is fully displayed."""
        self._add_text("", "separator")

        if exit_chat:
            self._add_text("🤖 StudyBuddy:", "bot_label")
            self._type_text_async(
                random.choice(GOODBYE_QUOTES),
                "bot_msg",
                callback=self._on_close
            )
            return

        self.input_entry.config(state=tk.NORMAL)
        self.send_btn.config(state=tk.NORMAL)
        self.input_entry.focus_set()

    def _on_close(self):
        """Handle window close."""
        self.root.destroy()


# -----------------------------
# Main Entry Point
# -----------------------------

def main():
    root = tk.Tk()
    app = StudyBuddyGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()