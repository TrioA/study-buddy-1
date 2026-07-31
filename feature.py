# ==========================================
# StudyBuddy Chatbot
# features.py
# ==========================================

# Imports
import re
import random
import math
import statistics
from datetime import datetime, timedelta

from data import *

# Maths functions
allowed_math = {

    "sqrt": math.sqrt,
    "pow": pow,
    "abs": abs,
    "round": round,

    "factorial": math.factorial,

    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,

    "log": math.log,
    "log10": math.log10,

    "ceil": math.ceil,
    "floor": math.floor,

    "gcd": math.gcd,
    "lcm": math.lcm,

    "pi": math.pi,
    "e": math.e

}

# Safe calculator
def calculate(expression):

    try:

        answer = eval(

            expression,

            {"__builtins__": None},

            allowed_math

        )

        return f"Answer : {answer}"

    except:

        return "I couldn't solve that calculation."

# Mean
def find_mean(numbers):

    try:

        return statistics.mean(numbers)

    except:

        return None

# Median
def find_median(numbers):

    try:

        return statistics.median(numbers)

    except:

        return None

# Mode
def find_mode(numbers):

    try:

        return statistics.mode(numbers)

    except:

        return None

# Percentage
def percentage(obtained, total):

    if total == 0:
        return None

    return round((obtained / total) * 100, 2)

# Study tips
def random_study_tip():

    subjects = list(SUBJECT_TIPS.keys())

    subject = random.choice(subjects)

    tip = random.choice(

        SUBJECT_TIPS[subject]["tips"]

    )

    return f"{subject.title()} Tip:\n{tip}"

# Motivation
def motivation():

    return random.choice(MOTIVATIONAL_QUOTES)

# Random fact
def fun_fact():

    return random.choice(FUN_FACTS)

# Career
def suggest_career(subject):

    subject = subject.lower()

    if subject in CAREERS:

        jobs = ", ".join(CAREERS[subject])

        return jobs

    return None

# Study method
def study_method(name):

    name = name.lower().replace(" ", "_")

    if name not in STUDY_METHODS:

        return None

    info = STUDY_METHODS[name]

    reply = ""

    reply += info["name"] + "\n\n"

    reply += info["description"] + "\n\n"

    reply += "Steps\n"

    for i, step in enumerate(info["steps"], 1):

        reply += f"{i}. {step}\n"

    reply += "\n"

    reply += "Best For : "

    reply += info["best_for"]

    return reply

# Subject tips
def subject_tip(subject):

    subject = subject.lower()

    if subject not in SUBJECT_TIPS:

        return None

    tips = SUBJECT_TIPS[subject]["tips"]

    reply = ""

    reply += subject.title()

    reply += " Study Tips\n\n"

    for i, tip in enumerate(tips, 1):

        reply += f"{i}. {tip}\n"

    return reply
# Numbers from text
def get_numbers(text):

    nums = re.findall(r"-?\d+\.?\d*", text)

    return [float(num) for num in nums]

# Maths helper
def maths_helper(text):

    text = text.lower()

    nums = get_numbers(text)

    # Square Root
    if "square root" in text or "sqrt" in text:

        if len(nums) >= 1:
            return f"Answer : {math.sqrt(nums[0])}"

    # Factorial
    if "factorial" in text:

        if len(nums) >= 1:
            return f"Answer : {math.factorial(int(nums[0]))}"

    # GCD / HCF
    if "gcd" in text or "hcf" in text:

        if len(nums) >= 2:
            return f"Answer : {math.gcd(int(nums[0]), int(nums[1]))}"

    # LCM
    if "lcm" in text:

        if len(nums) >= 2:
            return f"Answer : {math.lcm(int(nums[0]), int(nums[1]))}"

    # Mean
    if "mean" in text or "average" in text:

        if len(nums) >= 2:
            return f"Answer : {statistics.mean(nums)}"

    # Median
    if "median" in text:

        if len(nums) >= 2:
            return f"Answer : {statistics.median(nums)}"

    # Mode
    if "mode" in text:

        if len(nums) >= 2:

            try:
                return f"Answer : {statistics.mode(nums)}"

            except:
                return "There is no unique mode."

    # Percentage
    if "percentage" in text or "%" in text:

        if len(nums) >= 2:

            value = percentage(nums[0], nums[1])

            return f"Answer : {value}%"

    # Area of Circle
    if "area of circle" in text:

        if len(nums) >= 1:

            area = math.pi * nums[0] * nums[0]

            return f"Answer : {round(area,2)}"

    # Circumference
    if "circumference" in text:

        if len(nums) >= 1:

            c = 2 * math.pi * nums[0]

            return f"Answer : {round(c,2)}"

    # Basic Expression
    if any(op in text for op in ["+","-","*","/","(",")"]):

        return calculate(text)

    return None


# Countdown
def countdown(days):

    future = datetime.now() + timedelta(days=days)

    return future.strftime("%d %B %Y")


# Daily challenge
def daily_challenge():

    challenges = [

        "Revise one chapter today.",

        "Solve 20 Maths questions.",

        "Read for 30 minutes.",

        "Complete one pending homework.",

        "Learn five new English words.",

        "Practice one coding question."

    ]

    return random.choice(challenges)


# Homework help
def homework_help(subject):

    subject = subject.lower()

    if subject in HOMEWORK_GUIDE:

        return HOMEWORK_GUIDE[subject]

    return "Try understanding the concept first before writing the answer."


# Quick quiz
def random_quiz():

    if "QUIZ_QUESTIONS" not in globals():

        return None
# Quiz
def start_quiz(subject="general"):

    if "QUIZ_QUESTIONS" not in globals():
        return "Quiz database not found."

    if subject not in QUIZ_QUESTIONS:
        return "Quiz not available for this subject."

    questions = QUIZ_QUESTIONS[subject]
    score = 0

    print("\n🤖 Bot : Starting Quiz...\n")

    random.shuffle(questions)

    for q in questions[:5]:

        print(q["question"])

        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        try:
            ans = int(input("\nYour Answer (1-4): "))

            if ans == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Correct Answer : {q['answer']}\n")

        except:
            print("❌ Invalid Input\n")

    return f"Quiz Finished!\nYour Score : {score}/5"


# Study planner
def create_plan(hours):

    try:
        hours = float(hours)
    except:
        return "Please enter valid study hours."

    plan = []

    subjects = list(SUBJECT_TIPS.keys())

    random.shuffle(subjects)

    block = round(hours / len(subjects), 1)

    for subject in subjects:

        plan.append(
            f"{subject.title()} : {block} hour(s)"
        )

    return "\n".join(plan)


# Goal tracker
def goal_progress(done, total):

    try:

        done = int(done)
        total = int(total)

        if total == 0:
            return "Goal cannot be zero."

        percent = round(done / total * 100, 1)

        if percent >= 100:
            return "🎉 Goal Completed!"

        return f"Progress : {percent}%"

    except:
        return "Invalid values."


# Badge system
def get_badge(score):

    if score >= 95:
        return "🏆 Study Legend"

    if score >= 85:
        return "🥇 Gold Learner"

    if score >= 70:
        return "🥈 Silver Learner"

    if score >= 50:
        return "🥉 Bronze Learner"

    return "🌱 Beginner"


# Study streak
def update_streak(user):

    today = datetime.now().strftime("%d-%m-%Y")

    if user["last_login"] == today:
        return user["study_streak"]

    user["study_streak"] += 1
    user["last_login"] = today

    return user["study_streak"]


# Date and time
def current_time():

    return datetime.now().strftime("%d %B %Y | %I:%M %p")


# Random subject
def recommend_subject():

    return random.choice(list(SUBJECT_TIPS.keys()))


# Help menu
def help_menu():

    menu = [

        "Study Tips",
        "Homework Help",
        "Maths Solver",
        "Career Guidance",
        "Study Planner",
        "Motivation",
        "Quiz",
        "Fun Facts",
        "Calculator"

    ]

    return "\n".join(menu)
# Formula
def get_formula(topic):

    topic = topic.lower().replace(" ", "_")

    if topic not in FORMULAS:
        return None

    info = FORMULAS[topic]

    reply = ""

    reply += f"Formula : {info['formula']}\n"
    reply += f"Variables : {info['variables']}\n"
    reply += f"Chapter : {info['chapter']}\n"
    reply += f"Class : {info['class']}"

    return reply


# Science Fact
def science_fact():

    return random.choice(SCIENCE_FACTS)


# Grammar Tip
def grammar_tip():

    return random.choice(GRAMMAR_TIPS)


# Coding Tip
def coding_tip():

    return random.choice(CODING_TIPS)


# Daily Challenge
def daily_challenge():

    return random.choice(DAILY_CHALLENGES)


# Conversation Starter
def conversation_starter():

    return random.choice(CONVERSATION_STARTERS)


# Encouragement
def encourage():

    return random.choice(ENCOURAGEMENT)


# Success Message
def success():

    return random.choice(SUCCESS_MESSAGES)


# Goodbye
def goodbye():

    return random.choice(GOODBYE_QUOTES)


# Achievement
def achievement(name):

    return ACHIEVEMENTS.get(name, None)


# Help
def show_help():

    return HELP_TEXT
# Feature Router
FEATURES = {

    "science fact": science_fact,
    "science": science_fact,

    "grammar": grammar_tip,
    "english": grammar_tip,

    "coding": coding_tip,
    "python": coding_tip,

    "motivate": motivation,
    "motivation": motivation,

    "challenge": daily_challenge,

    "study tip": random_study_tip,
    "study tips": random_study_tip,
    "tip": random_study_tip,
    "tips": random_study_tip,

    "fact": fun_fact,
    "facts": fun_fact,
    "fun fact": fun_fact,

    "quiz": lambda: "I can quiz you! Tell me the subject, like maths, science, or general.",
    "homework": lambda: "I can help with homework. Tell me the subject and the question you want solved.",

    "help": show_help,

    "goodbye": goodbye

}


# Search Formula
def search_formula(text):

    text = text.lower()

    for name in FORMULAS:

        words = name.replace("_", " ")

        if words in text:

            return get_formula(name)

    return None


# Search Subject
def search_subject(text):

    text = text.lower()

    for subject in SUBJECT_TIPS:

        if subject in text:

            return subject_tip(subject)

    return None


# Search Career
def search_career(text):

    text = text.lower()

    for stream in CAREERS:

        if stream in text:

            jobs = suggest_career(stream)

            return f"Possible Careers:\n\n{jobs}"

    return None


# Main Feature Handler
def feature_reply(text):

    text = text.lower()

    replies = []

    # Formula
    formula = search_formula(text)

    if formula:
        replies.append(formula)

    # Subject Tips
    subject = search_subject(text)

    if subject:
        replies.append(subject)

    # Career
    career = search_career(text)

    if career:
        replies.append(career)

    # Built-in features
    for key in FEATURES:

        if key in text:

            replies.append(FEATURES[key]())

    # Maths
    maths = maths_helper(text)

    if maths:
        replies.append(maths)

    # Nothing found
    if not replies:

        return None

    return "\n\n".join(replies)


# About
def about():

    return (
        "StudyBuddy\n"
        "A rule-based study assistant built using Python.\n"
        "Features include quizzes, maths solving, study tips,\n"
        "career guidance, motivation and more."
    )
    return random.choice(QUIZ_QUESTIONS)
