# ==========================================
# StudyBuddy Chatbot
# Data File
# Version 3.0
# ==========================================

"""
This file stores all the information used by the chatbot.

It contains:
- Keywords
- Responses
- Study Methods
- Career Information
- Quotes
- Quiz Questions
- Facts

No chatbot logic is written here.
Only data is stored.
"""

# ==========================================
# Imports
# ==========================================

import random
from textwrap import fill


# ==========================================
# BOT INFORMATION
# ==========================================

BOT_NAME = "StudyBuddy"
BOT_VERSION = "3.0"

WELCOME_MESSAGE = [
    f"Hello! I'm {BOT_NAME}.",
    "I'm here to help you study smarter, not harder.",
    "You can ask me naturally, or choose a number from the menu.",
    "1 = Study Tips",
    "2 = Quote of the Day",
    "3 = Fact of the Day",
    "4 = Daily Challenge",
    "5 = Career Idea",
    "6 = Quiz",
    "7 = Homework Help",
    "8 = Maths Help",
    "9 = Study Plan"
]


# ==========================================
# INTENT KEYWORDS
# ==========================================

INTENT_KEYWORDS = {

    "greeting": [
        "hi", "hello", "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    "thanks": [
        "thanks",
        "thank you",
        "thx"
    ],

    "bye": [
        "bye",
        "goodbye",
        "see you",
        "exit",
        "quit",
        "close"
    ],

    "study": [
        "study",
        "studying",
        "learn",
        "learning",
        "revision",
        "revise",
        "exam",
        "exams",
        "test",
        "prepare",
        "school",
        "homework",
        "assignment",
        "focus",
        "concentrate"
    ],

    "time": [
        "time",
        "schedule",
        "routine",
        "planner",
        "manage",
        "busy",
        "late",
        "procrastinate",
        "timetable"
    ],

    "career": [
        "career",
        "future",
        "job",
        "profession",
        "doctor",
        "engineer",
        "scientist",
        "pilot",
        "lawyer",
        "teacher",
        "dream",
        "ambition",
        "stream",
        "college",
        "path"
    ],

    "homework": [
        "homework",
        "assignment",
        "worksheet",
        "project",
        "question",
        "solve",
        "answer"
    ],

    "motivation": [
        "sad",
        "stress",
        "stressed",
        "tired",
        "motivate",
        "motivation",
        "burnout",
        "demotivated",
        "upset",
        "discouraged",
        "lazy",
        "inspire",
        "confidence",
        "low"
    ],

    "quiz": [
        "quiz",
        "mcq",
        "test me",
        "practice",
        "questions"
    ],

    "math": [
        "math",
        "maths",
        "mathematics",
        "calculate",
        "equation",
        "formula",
        "percentage",
        "factorial",
        "square root",
        "lcm",
        "hcf",
        "gcd"
    ]

}


# ==========================================
# COMMON RESPONSES
# ==========================================

RESPONSES = {

    "greeting": [

        "Hello! 😊 How can I help you today?",

        "Hi there! Ready to learn something new?",

        "Welcome back! What are we studying today?",

        "Hey! It's always nice to see you again.",

        "Hello! Let's make today productive."

    ],

    "thanks": [

        "You're most welcome! 😊",

        "Happy to help!",

        "Glad I could help.",

        "You're welcome. Keep learning!",

        "Anytime! Good luck with your studies."

    ],

    "bye": [

        "Goodbye! Keep learning and stay curious.",

        "See you soon. Have a productive day!",

        "Best of luck with your studies!",

        "Take care and never stop learning.",

        "Bye! Remember, consistency beats perfection."

    ],

    "unknown": [

        "I'm still learning that topic. Could you ask it in another way?",

        "I don't fully understand yet, but I'm learning every day.",

        "Sorry, I couldn't understand that. Could you rephrase your question?",

        "Interesting question! Could you explain it a little differently?",

        "I'm not sure about that yet. Try asking with different words."

    ]

}


# ==========================================
# STUDY METHODS
# ==========================================

STUDY_METHODS = {

    "pomodoro": {

        "name": "Pomodoro Technique",

        "description":
        "Study for 25 minutes with complete focus, then take a 5-minute break.",

        "steps": [

            "Choose one task.",

            "Set a 25-minute timer.",

            "Study without distractions.",

            "Take a 5-minute break.",

            "Repeat four times before taking a longer break."

        ],

        "best_for":
        "Revision, homework, and avoiding procrastination."

    },

    "active_recall": {

        "name": "Active Recall",

        "description":
        "Test yourself instead of repeatedly reading your notes.",

        "steps": [

            "Read the topic once.",

            "Close the book.",

            "Write everything you remember.",

            "Check mistakes and repeat."

        ],

        "best_for":
        "Science, Social Science, Biology, and theory-heavy chapters."

    },

    "spaced_repetition": {

        "name": "Spaced Repetition",

        "description":
        "Revise information after increasing intervals instead of cramming.",

        "steps": [

            "Study today.",

            "Revise tomorrow.",

            "Revise after 3 days.",

            "Revise after one week."

        ],

        "best_for":
        "Long-term memory and board exam preparation."

    }

}
# ==========================================
# SUBJECT-WISE STUDY TIPS
# ==========================================

SUBJECT_TIPS = {

    "maths": {

        "tips": [

            "Understand the concept before memorising formulas.",

            "Solve at least 10-15 questions daily.",

            "Write every step neatly.",

            "Always check your final answer.",

            "Practice previous years' questions."

        ],

        "recommended_method": "active_recall"

    },

    "science": {

        "tips": [

            "Draw labelled diagrams.",

            "Understand the 'why' behind every concept.",

            "Revise formulas regularly.",

            "Make short notes after every chapter.",

            "Relate concepts to daily life."

        ],

        "recommended_method": "spaced_repetition"

    },

    "social science": {

        "tips": [

            "Prepare timelines for history.",

            "Use maps regularly for geography.",

            "Connect civics with real-life examples.",

            "Revise dates using flashcards.",

            "Practice writing long answers."

        ],

        "recommended_method": "active_recall"

    },

    "english": {

        "tips": [

            "Read for at least 20 minutes every day.",

            "Improve vocabulary by learning five new words daily.",

            "Practise grammar exercises.",

            "Write answers in your own words.",

            "Revise important literary devices."

        ],

        "recommended_method": "active_recall"

    },

    "computer": {

        "tips": [

            "Understand the logic instead of memorising code.",

            "Write small programs every day.",

            "Debug your own code.",

            "Practise tracing programs.",

            "Experiment with new ideas."

        ],

        "recommended_method": "learning_by_doing"

    }

}


# ==========================================
# CAREER DATABASE
# ==========================================

CAREERS = {

    "maths": [

        "Data Scientist",

        "Software Engineer",

        "Civil Engineer",

        "Mechanical Engineer",

        "Statistician",

        "Actuary",

        "Research Scientist"

    ],

    "science": [

        "Doctor",

        "Scientist",

        "Pharmacist",

        "Biotechnologist",

        "Environmental Scientist",

        "Forensic Expert"

    ],

    "commerce": [

        "Chartered Accountant",

        "Financial Analyst",

        "Investment Banker",

        "Business Consultant",

        "Entrepreneur"

    ],

    "humanities": [

        "Lawyer",

        "Journalist",

        "Psychologist",

        "Civil Services",

        "Teacher",

        "Professor"

    ]

}


# ==========================================
# MOTIVATIONAL QUOTES
# ==========================================

MOTIVATIONAL_QUOTES = [

    "Success is built one study session at a time.",

    "Discipline will take you where motivation cannot.",

    "Consistency beats intensity.",

    "Dream big. Start small. Stay consistent.",

    "Progress, not perfection.",

    "Your future self is watching your choices today.",

    "The best investment is the one you make in yourself.",

    "Every expert was once a beginner.",

    "Small improvements every day create remarkable results.",

    "You don't have to be the smartest. Just don't stop learning."

]


# ==========================================
# FUN FACTS
# ==========================================

FUN_FACTS = [

    "Your brain uses around 20% of your body's total energy.",

    "Octopuses have three hearts.",

    "Honey never spoils if stored properly.",

    "Lightning is hotter than the surface of the Sun.",

    "Bananas are technically berries, but strawberries aren't.",

    "A day on Venus is longer than its year.",

    "The Eiffel Tower becomes slightly taller during summer due to heat expansion.",

    "Sharks existed before trees."

]


# ==========================================
# HOMEWORK GUIDANCE
# ==========================================

HOMEWORK_GUIDE = {

    "maths":
    "Show every calculation step clearly before writing the final answer.",

    "science":
    "Use diagrams wherever possible and explain the concept in simple language.",

    "english":
    "Answer in your own words instead of copying directly from the textbook.",

    "social science":
    "Write answers in points with headings and important keywords.",

    "computer":
    "Explain the logic first and then write the program neatly."

}


# ==========================================
# HELP MENU
# ==========================================

HELP_MENU = [

    "Study Tips",

    "Time Management",

    "Homework Help",

    "Career Guidance",

    "Motivational Quotes",

    "Quiz",

    "Maths Helper",

    "General Knowledge",

    "Fun Facts"

]

# Error Messages

ERROR_MESSAGES = [

    "Sorry, I couldn't understand that.",

    "Could you ask your question in a different way?",

    "I'm still learning about that topic.",

    "Please try using different keywords.",

    "I don't have enough information to answer that.",

    "Let's try another way of asking.",

    "Hmm...I couldn't figure that out.",

    "That doesn't seem familiar to me yet."

]


# Quiz Questions

QUIZ_QUESTIONS = {

    "maths": [

        {
            "question":"What is √144?",
            "options":["10","12","14","16"],
            "answer":2
        },

        {
            "question":"What is 15 × 8 ?",
            "options":["110","120","130","140"],
            "answer":2
        },

        {
            "question":"The value of π is closest to:",
            "options":["2.14","3.14","4.13","3.41"],
            "answer":2
        },

        {
            "question":"How many degrees are there in a right angle?",
            "options":["45","60","90","180"],
            "answer":3
        },

        {
            "question":"What is 9² ?",
            "options":["18","72","81","99"],
            "answer":3
        },

        {
            "question":"What is the perimeter of a square with side length 6?",
            "options":["12","24","36","18"],
            "answer":2
        },

        {
            "question":"What is 2⁵ ?",
            "options":["10","16","32","64"],
            "answer":3
        },

        {
            "question":"What is the smallest prime number?",
            "options":["0","1","2","3"],
            "answer":3
        },

        {
            "question":"What is 15% of 200?",
            "options":["20","25","30","35"],
            "answer":3
        },

        {
            "question":"Sum of angles in a triangle is:",
            "options":["90°","180°","270°","360°"],
            "answer":2
        }

    ],

    "science":[

        {
            "question":"What is the SI unit of Force?",
            "options":["Joule","Newton","Pascal","Watt"],
            "answer":2
        },

        {
            "question":"Plants prepare food by:",
            "options":["Respiration","Photosynthesis","Digestion","Fermentation"],
            "answer":2
        },

        {
            "question":"Human blood is purified by:",
            "options":["Heart","Kidney","Lungs","Liver"],
            "answer":2
        },

        {
            "question":"The speed of light is approximately:",
            "options":["3×10⁸ m/s","3000 m/s","300 m/s","3×10⁶ m/s"],
            "answer":1
        },

        {
            "question":"Which gas is most abundant in air?",
            "options":["Oxygen","Nitrogen","Carbon Dioxide","Hydrogen"],
            "answer":2
        },

        {
            "question":"What chemical element has symbol 'O'?",
            "options":["Osmium","Gold","Oxygen","Oxide"],
            "answer":3
        },

        {
            "question":"Which organ pumps blood in human body?",
            "options":["Lungs","Heart","Brain","Liver"],
            "answer":2
        },

        {
            "question":"What is the chemical formula of water?",
            "options":["CO2","H2O","NaCl","O2"],
            "answer":2
        },

        {
            "question":"Powerhouse of the cell is:",
            "options":["Nucleus","Ribosome","Mitochondria","Chloroplast"],
            "answer":3
        },

        {
            "question":"Which planet is closest to the Sun?",
            "options":["Venus","Earth","Mercury","Mars"],
            "answer":3
        }

    ],

    "computer":[

        {
            "question":"CPU stands for:",
            "options":[
                "Central Processing Unit",
                "Computer Primary Unit",
                "Central Program Unit",
                "Computer Processing Utility"
            ],
            "answer":1
        },

        {
            "question":"Python is a:",
            "options":[
                "Programming Language",
                "Browser",
                "Database",
                "Operating System"
            ],
            "answer":1
        },

        {
            "question":"Which symbol starts a comment in Python?",
            "options":["//","#","<!--","*"],
            "answer":2
        },

        {
            "question":"Which loop repeats while a condition is True?",
            "options":["for","repeat","while","loop"],
            "answer":3
        },

        {
            "question":"Which function takes user input?",
            "options":["print()","input()","type()","read()"],
            "answer":2
        },

        {
            "question":"RAM stands for:",
            "options":[
                "Read Access Memory",
                "Random Access Memory",
                "Rapid Action Module",
                "Remote Access Machine"
            ],
            "answer":2
        },

        {
            "question":"Which storage is permanent?",
            "options":["RAM","Cache","ROM","Registers"],
            "answer":3
        },

        {
            "question":"1 Byte consists of how many bits?",
            "options":["4","8","16","32"],
            "answer":2
        },

        {
            "question":"Which keyword defines a function in Python?",
            "options":["function","def","func","define"],
            "answer":2
        },

        {
            "question":"HTML is used for creating:",
            "options":["Databases","Web pages","Operating Systems","Compilers"],
            "answer":2
        }

    ],

    "general":[

        {
            "question":"Capital of India?",
            "options":["Mumbai","Delhi","Kolkata","Chennai"],
            "answer":2
        },

        {
            "question":"How many continents are there?",
            "options":["5","6","7","8"],
            "answer":3
        },

        {
            "question":"Which planet is called the Red Planet?",
            "options":["Earth","Mars","Jupiter","Mercury"],
            "answer":2
        },

        {
            "question":"Largest ocean?",
            "options":["Atlantic","Indian","Pacific","Arctic"],
            "answer":3
        },

        {
            "question":"National bird of India?",
            "options":["Peacock","Parrot","Sparrow","Crow"],
            "answer":1
        },

        {
            "question":"How many colors are in a rainbow?",
            "options":["5","6","7","8"],
            "answer":3
        },

        {
            "question":"Who wrote the national anthem of India?",
            "options":["Rabindranath Tagore","Bankim Chandra Chatterjee","Sarojini Naidu","Mahatma Gandhi"],
            "answer":1
        },

        {
            "question":"Smallest state in India by area?",
            "options":["Sikkim","Goa","Tripura","Mizoram"],
            "answer":2
        },

        {
            "question":"Which is the longest river in the world?",
            "options":["Amazon","Nile","Ganga","Mississippi"],
            "answer":2
        },

        {
            "question":"How many days are in a leap year?",
            "options":["365","366","364","367"],
            "answer":2
        }

    ]

}
# Formula Database

FORMULAS = {

    "area_circle": {
        "formula": "π × r²",
        "variables": "r = radius",
        "chapter": "Mensuration",
        "class": "9"
    },

    "circumference": {
        "formula": "2 × π × r",
        "variables": "r = radius",
        "chapter": "Mensuration",
        "class": "9"
    },

    "area_rectangle": {
        "formula": "length × breadth",
        "variables": "l = length, b = breadth",
        "chapter": "Mensuration",
        "class": "9"
    },

    "area_square": {
        "formula": "side²",
        "variables": "side = length of one side",
        "chapter": "Mensuration",
        "class": "9"
    },

    "pythagoras": {
        "formula": "a² + b² = c²",
        "variables": "c = hypotenuse",
        "chapter": "Triangles",
        "class": "9"
    },

    "speed": {
        "formula": "Distance / Time",
        "variables": "S = Speed",
        "chapter": "Motion",
        "class": "9"
    },

    "density": {
        "formula": "Mass / Volume",
        "variables": "D = Density",
        "chapter": "Matter",
        "class": "9"
    },

    "force": {
        "formula": "Mass × Acceleration",
        "variables": "F = Force",
        "chapter": "Force and Laws of Motion",
        "class": "9"
    }

}


# Science Facts

SCIENCE_FACTS = [

    "The human brain contains nearly 86 billion neurons.",

    "Sound cannot travel through a vacuum.",

    "Lightning is hotter than the surface of the Sun.",

    "Water expands when it freezes.",

    "The Earth revolves around the Sun in about 365.25 days.",

    "DNA stands for Deoxyribonucleic Acid.",

    "Plants release oxygen during photosynthesis.",

    "The speed of light is approximately 3 × 10⁸ m/s.",

    "Gravity on the Moon is about one-sixth that of Earth.",

    "The SI unit of energy is the Joule."

]


# Grammar Tips

GRAMMAR_TIPS = [

    "Begin every sentence with a capital letter.",

    "End sentences with proper punctuation.",

    "Use 'their' for possession, 'there' for place, and 'they're' for 'they are'.",

    "Read your answer once before submitting.",

    "Avoid repeating the same word many times.",

    "Use paragraphs for long answers.",

    "Write in active voice whenever possible.",

    "Check subject-verb agreement."

]


# Coding Tips

CODING_TIPS = [

    "Write meaningful variable names.",

    "Indent your code properly.",

    "Test your program with different inputs.",

    "Read error messages carefully.",

    "Break large problems into smaller functions.",

    "Comment only where necessary.",

    "Keep your code simple and readable.",

    "Avoid repeating the same code."

]
# Daily Challenges

DAILY_CHALLENGES = [

    "Revise one Science chapter today.",

    "Solve 20 Maths questions.",

    "Read 10 pages of an English book.",

    "Learn 5 new vocabulary words.",

    "Practice Python for 30 minutes.",

    "Complete one pending homework.",

    "Revise yesterday's class notes.",

    "Teach a concept to someone else.",

    "Make short notes of one chapter.",

    "Solve one previous year question paper."

]


# Conversation Starters

CONVERSATION_STARTERS = [

    "How can I improve my Maths?",

    "Give me today's study challenge.",

    "Suggest a career for me.",

    "Help me make a timetable.",

    "Motivate me.",

    "Start a quiz.",

    "Tell me a science fact.",

    "Give me a coding tip.",

    "Show me a formula.",

    "Help me with homework."

]


# Achievement Messages

ACHIEVEMENTS = {

    "first_chat":
    "🎉 Congratulations! You've started your StudyBuddy journey.",

    "first_quiz":
    "🏅 Great! You completed your first quiz.",

    "five_quizzes":
    "🥈 Quiz Explorer - Completed 5 quizzes!",

    "ten_quizzes":
    "🥇 Quiz Champion - Completed 10 quizzes!",

    "perfect_score":
    "🌟 Excellent! You scored full marks!",

    "study_streak_3":
    "🔥 3-Day Study Streak!",

    "study_streak_7":
    "🔥 Incredible! 7-Day Study Streak!",

    "study_streak_30":
    "🏆 Amazing! 30-Day Study Streak!"

}


# Encouragement

ENCOURAGEMENT = [

    "Every expert was once a beginner.",

    "Progress is better than perfection.",

    "Keep going, you're improving every day.",

    "Mistakes help us learn.",

    "Believe in yourself.",

    "Stay curious and never stop learning.",

    "Success comes from consistency.",

    "One step at a time.",

    "Learning is a journey, not a race.",

    "Today's effort becomes tomorrow's success."

]


# Success Messages

SUCCESS_MESSAGES = [

    "Great job! ✅",

    "Excellent work! 🌟",

    "Well done! 🎉",

    "That's correct! 👏",

    "Fantastic! Keep it up!",

    "You're doing really well!",

    "Nice work!",

    "Brilliant answer!"

]


# Help Text

HELP_TEXT = """

Welcome to StudyBuddy!

You can ask things like:

• Hi
• Give me study tips
• Motivate me
• Start a quiz
• Solve 25*36
• Find square root of 144
• Tell me a science fact
• Give me a coding tip
• Help me with homework
• Suggest a career
• Show me a formula
• Make a study plan

Type 'bye' anytime to exit.

"""


# Goodbye Messages

GOODBYE_QUOTES = [

    "Keep learning. See you soon!",

    "Have a productive day!",

    "Stay curious and keep growing.",

    "Good luck with your studies!",

    "Learning never stops. Goodbye!"

]
# ==========================================
# StudyBuddy Chatbot
# Data File
# Version 3.0
# ==========================================

"""
This file stores all the information used by the chatbot.

It contains:
- Keywords
- Responses
- Study Methods
- Career Information
- Quotes
- Quiz Questions
- Facts

No chatbot logic is written here.
Only data is stored.
"""

# ==========================================
# Imports
# ==========================================

import random
from textwrap import fill


# ==========================================
# BOT INFORMATION
# ==========================================

BOT_NAME = "StudyBuddy"
BOT_VERSION = "3.0"

WELCOME_MESSAGE = [
    f"Hello! I'm {BOT_NAME}.",
    "I'm here to help you study smarter, not harder.",
    "You can ask me naturally, or choose a number from the menu.",
    "1 = Study Tips",
    "2 = Quote of the Day",
    "3 = Fact of the Day",
    "4 = Daily Challenge",
    "5 = Career Idea",
    "6 = Quiz",
    "7 = Homework Help",
    "8 = Maths Help",
    "9 = Study Plan"
]


# ==========================================
# INTENT KEYWORDS
# ==========================================

INTENT_KEYWORDS = {

    "greeting": [
        "hi", "hello", "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    "thanks": [
        "thanks",
        "thank you",
        "thx"
    ],

    "bye": [
        "bye",
        "goodbye",
        "see you",
        "exit",
        "quit",
        "close"
    ],

    "study": [
        "study",
        "studying",
        "learn",
        "learning",
        "revision",
        "revise",
        "exam",
        "exams",
        "test",
        "prepare",
        "school",
        "homework",
        "assignment",
        "focus",
        "concentrate"
    ],

    "time": [
        "time",
        "schedule",
        "routine",
        "planner",
        "manage",
        "busy",
        "late",
        "procrastinate",
        "timetable"
    ],

    "career": [
        "career",
        "future",
        "job",
        "profession",
        "doctor",
        "engineer",
        "scientist",
        "pilot",
        "lawyer",
        "teacher",
        "dream",
        "ambition",
        "stream",
        "college",
        "path"
    ],

    "homework": [
        "homework",
        "assignment",
        "worksheet",
        "project",
        "question",
        "solve",
        "answer"
    ],

    "motivation": [
        "sad",
        "stress",
        "stressed",
        "tired",
        "motivate",
        "motivation",
        "burnout",
        "demotivated",
        "upset",
        "discouraged",
        "lazy",
        "inspire",
        "confidence",
        "low"
    ],

    "quiz": [
        "quiz",
        "mcq",
        "test me",
        "practice",
        "questions"
    ],

    "math": [
        "math",
        "maths",
        "mathematics",
        "calculate",
        "equation",
        "formula",
        "percentage",
        "factorial",
        "square root",
        "lcm",
        "hcf",
        "gcd"
    ]

}


# ==========================================
# COMMON RESPONSES
# ==========================================

RESPONSES = {

    "greeting": [

        "Hello! 😊 How can I help you today?",

        "Hi there! Ready to learn something new?",

        "Welcome back! What are we studying today?",

        "Hey! It's always nice to see you again.",

        "Hello! Let's make today productive."

    ],

    "thanks": [

        "You're most welcome! 😊",

        "Happy to help!",

        "Glad I could help.",

        "You're welcome. Keep learning!",

        "Anytime! Good luck with your studies."

    ],

    "bye": [

        "Goodbye! Keep learning and stay curious.",

        "See you soon. Have a productive day!",

        "Best of luck with your studies!",

        "Take care and never stop learning.",

        "Bye! Remember, consistency beats perfection."

    ],

    "unknown": [

        "I'm still learning that topic. Could you ask it in another way?",

        "I don't fully understand yet, but I'm learning every day.",

        "Sorry, I couldn't understand that. Could you rephrase your question?",

        "Interesting question! Could you explain it a little differently?",

        "I'm not sure about that yet. Try asking with different words."

    ]

}


# ==========================================
# STUDY METHODS
# ==========================================

STUDY_METHODS = {

    "pomodoro": {

        "name": "Pomodoro Technique",

        "description":
        "Study for 25 minutes with complete focus, then take a 5-minute break.",

        "steps": [

            "Choose one task.",

            "Set a 25-minute timer.",

            "Study without distractions.",

            "Take a 5-minute break.",

            "Repeat four times before taking a longer break."

        ],

        "best_for":
        "Revision, homework, and avoiding procrastination."

    },

    "active_recall": {

        "name": "Active Recall",

        "description":
        "Test yourself instead of repeatedly reading your notes.",

        "steps": [

            "Read the topic once.",

            "Close the book.",

            "Write everything you remember.",

            "Check mistakes and repeat."

        ],

        "best_for":
        "Science, Social Science, Biology, and theory-heavy chapters."

    },

    "spaced_repetition": {

        "name": "Spaced Repetition",

        "description":
        "Revise information after increasing intervals instead of cramming.",

        "steps": [

            "Study today.",

            "Revise tomorrow.",

            "Revise after 3 days.",

            "Revise after one week."

        ],

        "best_for":
        "Long-term memory and board exam preparation."

    }

}
# ==========================================
# SUBJECT-WISE STUDY TIPS
# ==========================================

SUBJECT_TIPS = {

    "maths": {

        "tips": [

            "Understand the concept before memorising formulas.",

            "Solve at least 10-15 questions daily.",

            "Write every step neatly.",

            "Always check your final answer.",

            "Practice previous years' questions."

        ],

        "recommended_method": "active_recall"

    },

    "science": {

        "tips": [

            "Draw labelled diagrams.",

            "Understand the 'why' behind every concept.",

            "Revise formulas regularly.",

            "Make short notes after every chapter.",

            "Relate concepts to daily life."

        ],

        "recommended_method": "spaced_repetition"

    },

    "social science": {

        "tips": [

            "Prepare timelines for history.",

            "Use maps regularly for geography.",

            "Connect civics with real-life examples.",

            "Revise dates using flashcards.",

            "Practice writing long answers."

        ],

        "recommended_method": "active_recall"

    },

    "english": {

        "tips": [

            "Read for at least 20 minutes every day.",

            "Improve vocabulary by learning five new words daily.",

            "Practise grammar exercises.",

            "Write answers in your own words.",

            "Revise important literary devices."

        ],

        "recommended_method": "active_recall"

    },

    "computer": {

        "tips": [

            "Understand the logic instead of memorising code.",

            "Write small programs every day.",

            "Debug your own code.",

            "Practise tracing programs.",

            "Experiment with new ideas."

        ],

        "recommended_method": "learning_by_doing"

    }

}


# ==========================================
# CAREER DATABASE
# ==========================================

CAREERS = {

    "maths": [

        "Data Scientist",

        "Software Engineer",

        "Civil Engineer",

        "Mechanical Engineer",

        "Statistician",

        "Actuary",

        "Research Scientist"

    ],

    "science": [

        "Doctor",

        "Scientist",

        "Pharmacist",

        "Biotechnologist",

        "Environmental Scientist",

        "Forensic Expert"

    ],

    "commerce": [

        "Chartered Accountant",

        "Financial Analyst",

        "Investment Banker",

        "Business Consultant",

        "Entrepreneur"

    ],

    "humanities": [

        "Lawyer",

        "Journalist",

        "Psychologist",

        "Civil Services",

        "Teacher",

        "Professor"

    ]

}


# ==========================================
# MOTIVATIONAL QUOTES
# ==========================================

MOTIVATIONAL_QUOTES = [

    "Success is built one study session at a time.",

    "Discipline will take you where motivation cannot.",

    "Consistency beats intensity.",

    "Dream big. Start small. Stay consistent.",

    "Progress, not perfection.",

    "Your future self is watching your choices today.",

    "The best investment is the one you make in yourself.",

    "Every expert was once a beginner.",

    "Small improvements every day create remarkable results.",

    "You don't have to be the smartest. Just don't stop learning."

]


# ==========================================
# FUN FACTS
# ==========================================

FUN_FACTS = [

    "Your brain uses around 20% of your body's total energy.",

    "Octopuses have three hearts.",

    "Honey never spoils if stored properly.",

    "Lightning is hotter than the surface of the Sun.",

    "Bananas are technically berries, but strawberries aren't.",

    "A day on Venus is longer than its year.",

    "The Eiffel Tower becomes slightly taller during summer due to heat expansion.",

    "Sharks existed before trees."

]


# ==========================================
# HOMEWORK GUIDANCE
# ==========================================

HOMEWORK_GUIDE = {

    "maths":
    "Show every calculation step clearly before writing the final answer.",

    "science":
    "Use diagrams wherever possible and explain the concept in simple language.",

    "english":
    "Answer in your own words instead of copying directly from the textbook.",

    "social science":
    "Write answers in points with headings and important keywords.",

    "computer":
    "Explain the logic first and then write the program neatly."

}


# ==========================================
# HELP MENU
# ==========================================

HELP_MENU = [

    "Study Tips",

    "Time Management",

    "Homework Help",

    "Career Guidance",

    "Motivational Quotes",

    "Quiz",

    "Maths Helper",

    "General Knowledge",

    "Fun Facts"

]

# Error Messages

ERROR_MESSAGES = [

    "Sorry, I couldn't understand that.",

    "Could you ask your question in a different way?",

    "I'm still learning about that topic.",

    "Please try using different keywords.",

    "I don't have enough information to answer that.",

    "Let's try another way of asking.",

    "Hmm...I couldn't figure that out.",

    "That doesn't seem familiar to me yet."

]


# Quiz Questions

QUIZ_QUESTIONS = {

    "maths": [

        {
            "question":"What is √144?",
            "options":["10","12","14","16"],
            "answer":2
        },

        {
            "question":"What is 15 × 8 ?",
            "options":["110","120","130","140"],
            "answer":2
        },

        {
            "question":"The value of π is closest to:",
            "options":["2.14","3.14","4.13","3.41"],
            "answer":2
        },

        {
            "question":"How many degrees are there in a right angle?",
            "options":["45","60","90","180"],
            "answer":3
        },

        {
            "question":"What is 9² ?",
            "options":["18","72","81","99"],
            "answer":3
        }

    ],

    "science":[

        {
            "question":"What is the SI unit of Force?",
            "options":["Joule","Newton","Pascal","Watt"],
            "answer":2
        },

        {
            "question":"Plants prepare food by:",
            "options":["Respiration","Photosynthesis","Digestion","Fermentation"],
            "answer":2
        },

        {
            "question":"Human blood is purified by:",
            "options":["Heart","Kidney","Lungs","Liver"],
            "answer":2
        },

        {
            "question":"The speed of light is approximately:",
            "options":["3×10⁸ m/s","3000 m/s","300 m/s","3×10⁶ m/s"],
            "answer":1
        },

        {
            "question":"Which gas is most abundant in air?",
            "options":["Oxygen","Nitrogen","Carbon Dioxide","Hydrogen"],
            "answer":2
        }

    ],

    "computer":[

        {
            "question":"CPU stands for:",
            "options":[
                "Central Processing Unit",
                "Computer Primary Unit",
                "Central Program Unit",
                "Computer Processing Utility"
            ],
            "answer":1
        },

        {
            "question":"Python is a:",
            "options":[
                "Programming Language",
                "Browser",
                "Database",
                "Operating System"
            ],
            "answer":1
        },

        {
            "question":"Which symbol starts a comment in Python?",
            "options":["//","#","<!--","*"],
            "answer":2
        },

        {
            "question":"Which loop repeats while a condition is True?",
            "options":["for","repeat","while","loop"],
            "answer":3
        },

        {
            "question":"Which function takes user input?",
            "options":["print()","input()","type()","read()"],
            "answer":2
        }

    ],

    "general":[

        {
            "question":"Capital of India?",
            "options":["Mumbai","Delhi","Kolkata","Chennai"],
            "answer":2
        },

        {
            "question":"How many continents are there?",
            "options":["5","6","7","8"],
            "answer":3
        },

        {
            "question":"Which planet is called the Red Planet?",
            "options":["Earth","Mars","Jupiter","Mercury"],
            "answer":2
        },

        {
            "question":"Largest ocean?",
            "options":["Atlantic","Indian","Pacific","Arctic"],
            "answer":3
        },

        {
            "question":"National bird of India?",
            "options":["Peacock","Parrot","Sparrow","Crow"],
            "answer":1
        }

    ]

}
# Formula Database

FORMULAS = {

    "area_circle": {
        "formula": "π × r²",
        "variables": "r = radius",
        "chapter": "Mensuration",
        "class": "9"
    },

    "circumference": {
        "formula": "2 × π × r",
        "variables": "r = radius",
        "chapter": "Mensuration",
        "class": "9"
    },

    "area_rectangle": {
        "formula": "length × breadth",
        "variables": "l = length, b = breadth",
        "chapter": "Mensuration",
        "class": "9"
    },

    "area_square": {
        "formula": "side²",
        "variables": "side = length of one side",
        "chapter": "Mensuration",
        "class": "9"
    },

    "pythagoras": {
        "formula": "a² + b² = c²",
        "variables": "c = hypotenuse",
        "chapter": "Triangles",
        "class": "9"
    },

    "speed": {
        "formula": "Distance / Time",
        "variables": "S = Speed",
        "chapter": "Motion",
        "class": "9"
    },

    "density": {
        "formula": "Mass / Volume",
        "variables": "D = Density",
        "chapter": "Matter",
        "class": "9"
    },

    "force": {
        "formula": "Mass × Acceleration",
        "variables": "F = Force",
        "chapter": "Force and Laws of Motion",
        "class": "9"
    }

}


# Science Facts

SCIENCE_FACTS = [

    "The human brain contains nearly 86 billion neurons.",

    "Sound cannot travel through a vacuum.",

    "Lightning is hotter than the surface of the Sun.",

    "Water expands when it freezes.",

    "The Earth revolves around the Sun in about 365.25 days.",

    "DNA stands for Deoxyribonucleic Acid.",

    "Plants release oxygen during photosynthesis.",

    "The speed of light is approximately 3 × 10⁸ m/s.",

    "Gravity on the Moon is about one-sixth that of Earth.",

    "The SI unit of energy is the Joule."

]


# Grammar Tips

GRAMMAR_TIPS = [

    "Begin every sentence with a capital letter.",

    "End sentences with proper punctuation.",

    "Use 'their' for possession, 'there' for place, and 'they're' for 'they are'.",

    "Read your answer once before submitting.",

    "Avoid repeating the same word many times.",

    "Use paragraphs for long answers.",

    "Write in active voice whenever possible.",

    "Check subject-verb agreement."

]


# Coding Tips

CODING_TIPS = [

    "Write meaningful variable names.",

    "Indent your code properly.",

    "Test your program with different inputs.",

    "Read error messages carefully.",

    "Break large problems into smaller functions.",

    "Comment only where necessary.",

    "Keep your code simple and readable.",

    "Avoid repeating the same code."

]
# Daily Challenges

DAILY_CHALLENGES = [

    "Revise one Science chapter today.",

    "Solve 20 Maths questions.",

    "Read 10 pages of an English book.",

    "Learn 5 new vocabulary words.",

    "Practice Python for 30 minutes.",

    "Complete one pending homework.",

    "Revise yesterday's class notes.",

    "Teach a concept to someone else.",

    "Make short notes of one chapter.",

    "Solve one previous year question paper."

]


# Conversation Starters

CONVERSATION_STARTERS = [

    "How can I improve my Maths?",

    "Give me today's study challenge.",

    "Suggest a career for me.",

    "Help me make a timetable.",

    "Motivate me.",

    "Start a quiz.",

    "Tell me a science fact.",

    "Give me a coding tip.",

    "Show me a formula.",

    "Help me with homework."

]


# Achievement Messages

ACHIEVEMENTS = {

    "first_chat":
    "🎉 Congratulations! You've started your StudyBuddy journey.",

    "first_quiz":
    "🏅 Great! You completed your first quiz.",

    "five_quizzes":
    "🥈 Quiz Explorer - Completed 5 quizzes!",

    "ten_quizzes":
    "🥇 Quiz Champion - Completed 10 quizzes!",

    "perfect_score":
    "🌟 Excellent! You scored full marks!",

    "study_streak_3":
    "🔥 3-Day Study Streak!",

    "study_streak_7":
    "🔥 Incredible! 7-Day Study Streak!",

    "study_streak_30":
    "🏆 Amazing! 30-Day Study Streak!"

}


# Encouragement

ENCOURAGEMENT = [

    "Every expert was once a beginner.",

    "Progress is better than perfection.",

    "Keep going, you're improving every day.",

    "Mistakes help us learn.",

    "Believe in yourself.",

    "Stay curious and never stop learning.",

    "Success comes from consistency.",

    "One step at a time.",

    "Learning is a journey, not a race.",

    "Today's effort becomes tomorrow's success."

]


# Success Messages

SUCCESS_MESSAGES = [

    "Great job! ✅",

    "Excellent work! 🌟",

    "Well done! 🎉",

    "That's correct! 👏",

    "Fantastic! Keep it up!",

    "You're doing really well!",

    "Nice work!",

    "Brilliant answer!"

]


# Help Text

HELP_TEXT = """

Welcome to StudyBuddy!

You can ask things like:

• Hi
• Give me study tips
• Motivate me
• Start a quiz
• Solve 25*36
• Find square root of 144
• Tell me a science fact
• Give me a coding tip
• Help me with homework
• Suggest a career
• Show me a formula
• Make a study plan

Type 'bye' anytime to exit.

"""


# Goodbye Messages

GOODBYE_QUOTES = [

    "Keep learning. See you soon!",

    "Have a productive day!",

    "Stay curious and keep growing.",

    "Good luck with your studies!",

    "Learning never stops. Goodbye!"

]
