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
    "history": []

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

            return json.load(file)

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

def type_text(message, speed=0.03):

    print("\n🤖 Bot : ", end="")

    for letter in message:

        print(letter, end="", flush=True)

        time.sleep(speed)

    print()

# -----------------------------
# Thinking Animation
# -----------------------------

def thinking_animation():

    print("\n🤖 Bot : Thinking", end="", flush=True)

    for i in range(3):

        time.sleep(0.35)

        print(".", end="", flush=True)

    print()

# -----------------------------
# Bot Reply
# -----------------------------

def bot_reply(message):

    thinking_animation()

    type_text(fill(str(message), width=75))

# -----------------------------
# Welcome
# -----------------------------

def welcome():

    print("=" * 55)
    print("📚          STUDYBUDDY CHATBOT")
    print("=" * 55)

    for line in WELCOME_MESSAGE:

        type_text(line)

    print()
    type_text("Type a number for quick help: 1 = Tips, 2 = Quote, 3 = Fact, 4 = Challenge, 5 = Career, 6 = Quiz, 7 = Homework, 8 = Maths, 9 = Study Plan")

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
    match = re.search(r"(my name is|i am|i'm)\s+([A-Za-z]+)", text, re.I)

    if match:

        user["name"] = match.group(2).title()

        return f"Nice to meet you, {user['name']}! I'll remember your name."

    # Favourite Subject
    match = re.search(
        r"(my favourite subject is|my favorite subject is|i like)\s+(.+)",
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
            "1. Study tip\n"
            "2. Quote of the day\n"
            "3. Fact of the day\n"
            "4. Daily challenge\n"
            "5. Career suggestion\n"
            "6. Start quiz\n"
            "7. Homework help\n"
            "8. Maths help\n"
            "9. Study plan"
        )

    if command in {"1", "one", "tip", "tips", "study tip", "study tips"}:

        topic = get_context_topic(user, text)

        if topic:

            return subject_tip(topic)

        return random_study_tip()

    if command in {"2", "two", "quote", "quote of the day", "motivation", "motivational quote"}:

        return f"Quote of the day:\n{motivation()}"

    if command in {"3", "three", "fact", "fact of the day", "fun fact"}:

        return f"Fact of the day:\n{fun_fact()}"

    if command in {"4", "four", "challenge", "daily challenge"}:

        return f"Daily challenge:\n{daily_challenge()}"

    if command in {"5", "five", "career", "career idea", "job idea"}:

        topic = get_context_topic(user, text)

        if not topic and user.get("favorite_subject"):

            topic = user["favorite_subject"].lower()

        if topic:

            jobs = suggest_career(topic)

            if jobs:

                return f"Career ideas for {topic.title()}:\n{jobs}"

        return "Tell me your favourite subject first, then I'll suggest suitable careers."

    if command in {"6", "six", "quiz", "start quiz"}:

        topic = get_context_topic(user, text) or "general"

        return start_quiz(topic)

    if command in {"7", "seven", "homework", "homework help"}:

        topic = get_context_topic(user, text)

        if topic:

            return homework_help(topic)

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

    # Subject Tips
    subject = detect_subject(text)

    if subject:

        return subject_tip(subject)

    # Study Methods
    method = detect_method(text)

    if method:

        return study_method(method)

    # Career Suggestions
    if "career" in intents:

        topic = get_context_topic(user, text)

        if not topic and user["favorite_subject"]:

            topic = user["favorite_subject"].lower()

        if topic:

            jobs = suggest_career(topic)

            if jobs:

                return (
                    f"Based on your favourite subject "
                    f"({topic.title()}), "
                    f"you may enjoy these careers:\n\n{jobs}"
                )

        return (
            "Tell me your favourite subject first, "
            "then I'll suggest suitable careers."
        )

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
