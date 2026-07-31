# ==========================================
# StudyBuddy Chatbot
# chatbot.py
# ==========================================

# Imports
import json
import random
import re
import time

from pathlib import Path
from datetime import datetime
from difflib import get_close_matches
from textwrap import fill

from data import *
from feature import *

# -----------------------------
# User Data
# -----------------------------

DATA_FILE = Path("user_data.json")

DEFAULT_USER = {

    "name": "",
    "class": "",
    "favorite_subject": "",
    "goal": "",
    "quiz_score": 0,
    "study_streak": 0,
    "last_login": "",
    "pending_context": {},
    "history": [],
    "first_run": True

}

# -----------------------------
# Load User
# -----------------------------

def load_user():

    if not DATA_FILE.exists():

        with open(DATA_FILE, "w") as file:

            json.dump(DEFAULT_USER, file, indent=4)

        return DEFAULT_USER.copy()

    try:

        with open(DATA_FILE, "r") as file:

            user = json.load(file)
            # Ensure pending_context and first_run exist for older user data
            if "pending_context" not in user:
                user["pending_context"] = {}
            if "first_run" not in user:
                user["first_run"] = False
            return user

    except:

        return DEFAULT_USER.copy()

# -----------------------------
# Save User
# -----------------------------

def save_user(user):

    with open(DATA_FILE, "w") as file:

        json.dump(user, file, indent=4)

# -----------------------------
# Bot Typing
# -----------------------------

# Global flag to track if typing should be skipped after Ctrl+C
SKIP_TYPING = False

def type_text(message, speed=0.03, prefix=""):
    global SKIP_TYPING

    print(prefix, end="")

    if SKIP_TYPING:
        print(message)
        return

    try:
        for letter in message:
            print(letter, end="", flush=True)
            time.sleep(speed)
        print()
    except KeyboardInterrupt:
        SKIP_TYPING = True
        # Print remainder of message immediately
        print(message[len(message):] if message.endswith(letter) else letter + message[message.index(letter)+1:])

# -----------------------------
# Thinking Animation
# -----------------------------

def thinking_animation():
    global SKIP_TYPING

    if SKIP_TYPING:
        return

    print("\n🤖 StudyBuddy: Thinking", end="", flush=True)

    try:
        for i in range(3):
            time.sleep(0.35)
            print(".", end="", flush=True)
        print()
    except KeyboardInterrupt:
        SKIP_TYPING = True
        print("...")

# -----------------------------
# Bot Reply
# -----------------------------

def bot_reply(message):
    global SKIP_TYPING
    SKIP_TYPING = False

    thinking_animation()

    lines = str(message).split("\n")

    for i, line in enumerate(lines):

        wrapped = fill(line, width=75)

        if i == 0:
            type_text(wrapped, prefix="🤖 StudyBuddy: ")
        else:
            type_text(wrapped, prefix="               ")

def get_user_instructions():
    """Load and format user_instructions.txt for startup display."""
    instructions_file = Path("user_instructions.txt")
    if not instructions_file.exists():
        return []

    try:
        with open(instructions_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        formatted = []
        for line in lines:
            if line.startswith("StudyBuddy User Instructions"):
                formatted.append("📖 " + line.upper())
            elif line.startswith("#"):
                # Clean "#1. text" to "• 1. text"
                clean_item = line.lstrip("#")
                formatted.append("  • " + clean_item)
            else:
                formatted.append(line)
        return formatted
    except Exception:
        return []

# -----------------------------
# Welcome
# -----------------------------

def welcome():
    global SKIP_TYPING
    SKIP_TYPING = False

    user = load_user()

    print("=" * 55)
    print("📚          STUDYBUDDY CHATBOT")
    print("=" * 55)

    for i, line in enumerate(WELCOME_MESSAGE):
        if i == 0:
            type_text(line, prefix="🤖 StudyBuddy: ")
        else:
            type_text(line, prefix="               ")

    if user.get("first_run", True):
        instructions = get_user_instructions()
        if instructions:
            type_text("", prefix="               ")
            for line in instructions:
                type_text(line, prefix="               ")
        user["first_run"] = False
        save_user(user)

# -----------------------------
# Spell Correction
# -----------------------------

def correct_word(word):

    all_words = []

    for words in INTENT_KEYWORDS.values():

        all_words.extend(words)

    match = get_close_matches(

        word,
        all_words,
        n=1,
        cutoff=0.80

    )

    if match:

        return match[0]

    return word

# -----------------------------
# Correct Sentence
# -----------------------------

def correct_input(text):

    words = text.lower().split()

    corrected = []

    for word in words:

        corrected.append(correct_word(word))

    return " ".join(corrected)

# -----------------------------
# Detect Intent
# -----------------------------

def detect_intents(text):

    text = correct_input(text)

    intents = []

    for intent, words in INTENT_KEYWORDS.items():

        if any(word in text for word in words):

            intents.append(intent)

    return intents

# -----------------------------
# Update History
# -----------------------------

def update_history(user, message):

    now = datetime.now().strftime("%d-%m-%Y %H:%M")

    user["history"].append({

        "time": now,
        "message": message

    })

    if len(user["history"]) > 20:

        user["history"].pop(0)

# -----------------------------
# Exit Check
# -----------------------------

def should_exit(intents):

    return "bye" in intents

# -----------------------------
# Random Response
# -----------------------------

def get_response(intent):

    if intent in RESPONSES:

        return random.choice(RESPONSES[intent])

    return random.choice(ERROR_MESSAGES)

# -----------------------------
# Detect Subject
# -----------------------------

def detect_subject(text):

    text = text.lower()

    for subject in SUBJECT_TIPS:

        if re.search(rf"\b{re.escape(subject)}\b", text):

            return subject

    return None

# -----------------------------
# Detect Study Method
# -----------------------------

def detect_method(text):

    text = text.lower()

    for method in STUDY_METHODS:

        if method.replace("_", " ") in text:

            return method

# -----------------------------
# Remember Information
# -----------------------------
def remember_info(user, text):

    text = text.strip()

    # Name
    match = re.search(r"(my name is|i am|i'm|im)\s+([A-Za-z]+)", text, re.I)

    if match:

        user["name"] = match.group(2).title()

        return f"Nice to meet you, {user['name']}! I'll remember your name."

    # Favourite Subject
    match = re.search(
        r"(my favourite subject is|my favorite subject is|my fav subject is|i like)\s+(.+)",
        text,
        re.I
    )

    if match:

        subject = match.group(2).strip().title()

        user["favorite_subject"] = subject

        return f"Great! I'll remember that your favourite subject is {subject}."

    # Goal
    match = re.search(
        r"(my goal is|i want to become|i want to be)\s+(.+)",
        text,
        re.I
    )

    if match:

        goal = match.group(2).strip().title()

        user["goal"] = goal

        return f"That's a wonderful goal! I'll remember that you want to become {goal}."

    return None


# -----------------------------
# Answer Memory
# -----------------------------
def answer_memory(user, text):

    text = text.lower()

    if "what is my name" in text:

        if user["name"]:

            return f"Your name is {user['name']}."

        return "You haven't told me your name yet."

    if "favourite subject" in text or "favorite subject" in text:

        if user["favorite_subject"]:

            return f"Your favourite subject is {user['favorite_subject']}."

        return "You haven't told me your favourite subject yet."

    if "my goal" in text:

        if user["goal"]:

            return f"Your goal is to become {user['goal']}."

        return "You haven't shared your goal yet."

    return None


# -----------------------------
# Pending Context Handler
# -----------------------------
def handle_pending(user, text):

    pending = user.get("pending_context", {})
    if not pending:
        return None

    pending_type = pending.get("type")
    text_lower = text.lower().strip()

    # Career subject pending
    if pending_type == "awaiting_career_subject":

        for subject in CAREERS:
            if subject in text_lower or text_lower == subject:
                jobs = suggest_career(subject)
                if jobs:
                    user["favorite_subject"] = subject.title()
                    user["pending_context"] = {}
                    return f"Career ideas for {subject.title()}:\n{jobs}"

        user["pending_context"] = {}
        return "I'm not sure about careers for that. Try a subject like maths, science, or commerce."

    # Homework subject pending
    if pending_type == "awaiting_homework_subject":

        for subject in HOMEWORK_GUIDE:
            if subject in text_lower or text_lower == subject:
                user["pending_context"] = {}
                return homework_help(subject)

        user["pending_context"] = {}
        return "I have homework help for maths, science, english, social science, and computer."

    return None


# -----------------------------
# Context Helper
# -----------------------------
def get_context_topic(user, text):

    text = text.lower()
    history_messages = [entry.get("message", "") for entry in user.get("history", [])[-5:]]
    combined_text = " ".join(history_messages + [text])

    for subject in SUBJECT_TIPS:

        if re.search(rf"\b{re.escape(subject)}\b", combined_text):

            return subject

    favorite_subject = user.get("favorite_subject", "").strip().lower()

    if favorite_subject:

        normalized_favorite = favorite_subject.replace(" ", "")

        for subject in SUBJECT_TIPS:

            if subject.replace(" ", "") == normalized_favorite:

                return subject

    if any(word in text for word in ["tip", "tips", "study", "homework", "quiz", "plan", "career", "job", "future", "motivate", "quote", "fact", "challenge"]):

        for subject in SUBJECT_TIPS:

            if subject in text:

                return subject

    return None


# -----------------------------
# Quick Menu Handler
# -----------------------------
def handle_menu_command(user, text):

    command = text.strip().lower()

    if command in {"menu", "help", "0", "show menu"}:

        return (
            "Choose a number:\n"
            " 1 = Study Tips\n"
            " 2 = Quote of the Day\n"
            " 3 = Fact of the Day\n"
            " 4 = Daily Challenge\n"
            " 5 = Career Idea\n"
            " 6 = Quiz\n"
            " 7 = Homework Help\n"
            " 8 = Maths Help\n"
            " 9 = Study Plan"
        )

    if command in {"1", "one", "tip", "tips", "study tip", "study tips"}:

        topic = get_context_topic(user, text)

        if topic:

            return subject_tip(topic)

        return random_study_tip()

    if command in {"2", "two", "quote", "quote of the day", "motivation", "motivational quote"}:
        if (command.__contains__("day")):
            index = (today_num*197824) % len(MOTIVATIONAL_QUOTES)
            return f"Quote of the day:\n{MOTIVATIONAL_QUOTES[index]}"

        return f"Quote of the day:\n{motivation()}"

    if command in {"3", "three", "fact", "fact of the day", "fun fact"}:
        if (command.__contains__("day") or command.__contains__("3")):
            index = (today_num*348742) % len(FUN_FACTS)
            return f"Fact of the day:\n{FUN_FACTS[index]}"
        return f"Fact of the day:\n{fun_fact()}"

    if command in {"4", "four", "challenge", "daily challenge"}:

        return f"Daily challenge:\n{daily_challenge()}"

    if command in {"five", "career", "career idea", "job idea"} or "career" in command or command.startswith("5 "):


        # Try extracting subject from query text (e.g. 'career science', 'science career', '5 science', 'science 5')
        topic = detect_subject(text) or detect_subject(command)

        if not topic:
            topic = get_context_topic(user, text)

        if not topic and user.get("favorite_subject"):
            topic = user["favorite_subject"].lower()

        if topic:
            jobs = suggest_career(topic)
            if jobs:
                return f"Career ideas for {topic.title()}:\n{jobs}"

        # Ask the user for their subject and remember the conversation state
        user["pending_context"] = {"type": "awaiting_career_subject"}
        return "Tell me your favourite subject first, then I'll suggest suitable careers."

    if command in {"6", "six", "quiz", "start quiz"} or "quiz" in command or command.startswith("6 ") or command.endswith(" 6"):

        # Extract number of questions if provided (e.g. "quiz 5", "quiz 10", "6 3", "maths quiz 8")
        num_match = re.search(r"\b(\d+)\b", text)
        num_questions = 5
        if num_match:
            val = int(num_match.group(1))
            # Ignore option selection '6' if it was part of "6" command unless it's explicitly "quiz 6"
            if val != 6 or "quiz 6" in text.lower() or text.strip() == "6":
                if val != 6 or "quiz 6" in text.lower():
                    num_questions = val

        topic = detect_subject(text) or get_context_topic(user, text) or "general"

        return start_quiz(topic, num_questions=num_questions)

    if command in {"7", "seven", "homework", "homework help"} or re.match(r"^7\s+\w+", command):

        topic = get_context_topic(user, text)

        # Also try extracting subject directly from "7 maths" style commands
        if not topic:
            match = re.match(r"^7\s+(.+)", command)
            if match:
                subj = match.group(1).strip()
                for subject in HOMEWORK_GUIDE:
                    if subject in subj or subj == subject:
                        topic = subject
                        break

        if topic:

            return homework_help(topic)

        # Ask the user for their subject and remember the conversation state
        user["pending_context"] = {"type": "awaiting_homework_subject"}
        return "Tell me the subject for homework help, like maths or science."

    if command in {"8", "eight", "math", "maths", "math help", "solve"}:

        return "Ask me a maths question like 'what is the square root of 144?' or 'what is 20% of 80?'"

    if command in {"9", "nine", "plan", "study plan"}:

        return create_plan(3)

    return None


# -----------------------------
# Build Reply
# -----------------------------
def build_reply(user, intents, text):

    # Save personal information
    memory = remember_info(user, text)

    if memory:

        return memory

    # Recall information
    memory = answer_memory(user, text)

    if memory:

        return memory

    # Check pending context (conversation flow tracking)
    pending_reply = handle_pending(user, text)

    if pending_reply:

        return pending_reply

    menu_reply = handle_menu_command(user, text)

    if menu_reply:

        return menu_reply

    # Greetings
    if "greeting" in intents:

        return get_response("greeting")

    # Thanks
    if "thanks" in intents:

        return get_response("thanks")

    # Goodbye
    if "bye" in intents:

        return get_response("bye")

    # Hidden Commands
    lower_text = text.lower()

    if lower_text.strip() in {"instruction", "instructions", "show instructions", "help instructions"}:
        instructions = get_user_instructions()
        if instructions:
            return "\n".join(instructions)
        return "No instructions file found."

    if "who made you" in lower_text or \
       "who created you" in lower_text or \
       "who developed you" in lower_text:

        return (
            "I am StudyBuddy, a rule-based educational chatbot built entirely "
            "using Python.\n\n"
            "I was designed and developed by "
            "Amoli Agrawal (Class 9) and "
            "Arav Gupta (Class 10)."
        )

    if "about" == lower_text.strip():

        return about()

    if "version" in lower_text:

        return "StudyBuddy Version 3.0"

    if "features" in lower_text:

        return (
            "• Study Tips\n"
            "• Maths Solver\n"
            "• Homework Help\n"
            "• Career Guidance\n"
            "• Quizzes\n"
            "• Formula Search\n"
            "• Coding Tips\n"
            "• Science Facts\n"
            "• Grammar Tips\n"
            "• Daily Challenges"
        )

    if "help" == lower_text.strip():

        return show_help()

    # Career Suggestions
    if "career" in intents or "career" in text.lower() or "job" in text.lower():

        topic = detect_subject(text) or get_context_topic(user, text)

        if not topic and user.get("favorite_subject"):

            topic = user["favorite_subject"].lower()

        if topic:

            jobs = suggest_career(topic)

            if jobs:

                return f"Career ideas for {topic.title()}:\n{jobs}"

        return (
            "Tell me your favourite subject first, "
            "then I'll suggest suitable careers."
        )

    # Subject Tips
    subject = detect_subject(text)

    if subject:

        return subject_tip(subject)

    # Study Methods
    method = detect_method(text)

    if method:

        return study_method(method)

    # Motivation support
    if any(word in lower_text for word in ["stress", "tired", "sad", "burnout", "discouraged", "lazy", "demotivated"]):

        return (
            "That sounds tough, but you can get through it.\n"
            "Try one small step right now: review one page, solve one problem, or take a 5-minute break.\n"
            f"{motivation()}"
        )

    # All Remaining Features
    reply = feature_reply(text)

    if reply:

        return reply

    # Unknown
    return get_response("unknown")

# -----------------------------
# Chat
# -----------------------------
def chat(user_input):

    user = load_user()

    update_history(user, user_input)

    clean_text = correct_input(user_input)

    intents = detect_intents(clean_text)

    reply = build_reply(user, intents, clean_text)

    bot_reply(reply)

    save_user(user)

    return should_exit(intents)


# -----------------------------
# Start Chatbot
# -----------------------------
def start_chatbot():

    welcome()
    last_interrupt_time = 0

    while True:

        try:

            user_input = input("\n👤 You : ").strip()

            if not user_input:

                bot_reply(
                    "Please type something."
                )

                continue

            exit_chat = chat(user_input)

            if exit_chat:

                break

        except KeyboardInterrupt:

            now = time.time()
            if now - last_interrupt_time < 2.0:
                print("\n\nGoodbye! Exiting...")
                break
            last_interrupt_time = now

            print()

            bot_reply(
                random.choice(GOODBYE_QUOTES)
            )

            break

        except Exception:

            bot_reply(
                random.choice(ERROR_MESSAGES)
            )


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":

    start_chatbot()