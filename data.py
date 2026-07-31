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
    "9 = Study Plan",
    "You can also ask for a formula, science fact, coding tip, grammar tip, career idea, motivation, or subject-specific help."
]


# ==========================================
# INTENT KEYWORDS
# ==========================================

INTENT_KEYWORDS = {
    "greeting": ["hi","hello","hey","hii","hiii","heyy","helo","yo","sup","hiya","good morning","good afternoon","good evening","morning","afternoon","evening","how are you","how r u","what's up","whats up"],
    "thanks": ["thanks","thank you","thankyou","thx","ty","tys","thanks a lot","thank u","appreciate it","much appreciated","cheers"],
    "bye": ["bye","goodbye","good bye","see you","see ya","cya","later","exit","quit","close","leave","end chat"],
    "study": ["study","studying","studied","learn","learning","revision","revise","revising","review","recap","exam","exams","test","tests","prepare","preparation","school","class","homework","assignment","project","notes","chapter","lesson","syllabus","subject","textbook","worksheet","practice","practice questions","question paper","sample paper","previous year","pyq","board exam","boards","preboard","pre-board","focus","concentrate","concentration","memorise","memorize","remember","understand","concept","concepts","education","academics","academia"],
    "time": ["time","schedule","routine","planner","plan","manage","management","busy","late","procrastinate","procrastination","timetable","time table","calendar","deadline","deadlines","hours","hour","daily plan","weekly plan","study schedule","study routine","wasting time","can't focus","cant focus","distracted","distraction"],
    "career": ["career","future","job","jobs","profession","doctor","engineer","scientist","pilot","lawyer","teacher","architect","designer","developer","programmer","accountant","ca","entrepreneur","business","journalist","psychologist","researcher","dream","ambition","goal","goals","stream","streams","college","university","course","degree","path","career path","what should i become","what career","career options","career choice","career guidance","career advice","pcm","pcb","pcmb","commerce","humanities","arts","science stream"],
    "homework": ["homework","assignment","worksheet","project","question","questions","solve","solution","answer","answers","doubt","doubts","help me solve","explain this","explain question","step by step","working","calculation","problem","problems","exercise","exercise question","chapter question","schoolwork","classwork"],
    "motivation": ["sad","stress","stressed","stressful","tired","motivate","motivation","motivated","burnout","burnt out","demotivated","demotivated","upset","discouraged","lazy","inspire","inspiration","confidence","confident","low","low motivation","can't study","cant study","don't feel like studying","dont feel like studying","give up","giving up","overwhelmed","pressure","exam stress","study stress","procrastinating","unproductive","failure","failed","mistake","mistakes","nervous","anxious about exam","scared of exam"],
    "quiz": ["quiz","quizzes","mcq","mcqs","multiple choice","test me","quiz me","ask me questions","practice test","mock test","practice quiz","questions","trivia","challenge me","knowledge test","start quiz","give me a quiz"],
    "math": ["math","maths","mathematics","calculate","calculation","calculator","equation","equations","formula","formulas","formulae","percentage","percent","factorial","square root","cube root","root","lcm","hcf","gcd","algebra","polynomial","linear equation","quadratic","geometry","mensuration","trigonometry","trigonometric","sin","cos","tan","statistics","probability","mean","median","mode","ratio","proportion","fraction","decimal","integers","rational numbers","irrational numbers","coordinate geometry","area","perimeter","volume","surface area","theorem","pythagoras","pi","π","slope","graph","simplify","factorise","factorize","expand","solve for x"]
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
        "Hello! Let's make today productive.",
        "Hey! StudyBuddy is ready. What do you want to work on?",
        "Hi! Pick a subject, ask a doubt, or start a quiz.",
        "Hey there! Maths, Science, coding, homework, or motivation?"
    ],
    "thanks": [
        "You're most welcome! 😊","Happy to help!","Glad I could help.","You're welcome. Keep learning!","Anytime! Good luck with your studies.","No problem!","Absolutely! Keep going.","You got this! 📚","Always happy to help with studying."
    ],
    "bye": [
        "Goodbye! Keep learning and stay curious.","See you soon. Have a productive day!","Best of luck with your studies!","Take care and never stop learning.","Bye! Remember, consistency beats perfection.","See you next time! Keep that curiosity alive.","Good luck with your next study session!"
    ],
    "unknown": [
        "I'm still learning that topic. Could you ask it in another way?",
        "I don't fully understand yet, but I'm learning every day.",
        "Sorry, I couldn't understand that. Could you rephrase your question?",
        "Interesting question! Could you explain it a little differently?",
        "I'm not sure about that yet. Try asking with different words.",
        "I didn't catch the exact intent. Try mentioning the subject or task.",
        "Try something like 'give me a Maths quiz', 'explain photosynthesis', or 'help me plan my study time'.",
        "Hmm... I need a little more context. Tell me what subject or topic you're working on."
    ]
}


# ==========================================
# STUDY METHODS
# ==========================================

STUDY_METHODS = {
    "pomodoro": {
        "name": "Pomodoro Technique",
        "description": "Study for 25 minutes with complete focus, then take a 5-minute break. Adjust the work interval if needed.",
        "steps": ["Choose one clear task.","Set a 25-minute timer.","Study without distractions.","Take a 5-minute break.","Repeat four times, then take a longer break.","Record what you completed before starting the next cycle."],
        "best_for": "Revision, homework, focused practice, and reducing procrastination."
    },
    "active_recall": {
        "name": "Active Recall",
        "description": "Test yourself instead of repeatedly rereading notes. Retrieval strengthens memory.",
        "steps": ["Read the topic once.","Close the book.","Ask yourself questions or write everything you remember.","Check your notes for gaps.","Correct mistakes.","Repeat later without looking at the answer."],
        "best_for": "Science, Social Science, Biology, definitions, formulas, vocabulary, and theory-heavy chapters."
    },
    "spaced_repetition": {
        "name": "Spaced Repetition",
        "description": "Revise information after increasing intervals instead of cramming everything at once.",
        "steps": ["Study today.","Review tomorrow.","Review after 3 days.","Review after about a week.","Review again before the exam.","Increase the interval when recall becomes easy."],
        "best_for": "Long-term memory, formulas, vocabulary, dates, definitions, and board exam preparation."
    },
    "blurting": {
        "name": "Blurting",
        "description": "Recall everything you know about a topic from memory, then compare it with your notes.",
        "steps": ["Study a small section.","Close the book.","Write or say everything you remember.","Compare with your notes.","Fill missing points.","Repeat after a gap."],
        "best_for": "Theory chapters, Science, Social Science, Biology, and last-minute recall checks."
    },
    "feynman": {
        "name": "Feynman Technique",
        "description": "Explain a concept in very simple language as if teaching someone who has never seen it before.",
        "steps": ["Choose one concept.","Explain it using simple words.","Notice where your explanation becomes vague.","Return to the source and fix the gap.","Explain it again without jargon."],
        "best_for": "Difficult concepts, Physics, Maths reasoning, Science, and anything you can understand but cannot explain."
    },
    "interleaving": {
        "name": "Interleaved Practice",
        "description": "Mix related problem types instead of solving a large block of identical questions.",
        "steps": ["Choose 2-4 related question types.","Mix them in one practice set.","Identify which method each question needs.","Solve without relying on the previous question's pattern.","Review errors by type."],
        "best_for": "Maths, Physics, problem solving, and exam preparation."
    },
    "learning_by_doing": {
        "name": "Learning by Doing",
        "description": "Learn through practice, experiments, projects, coding, examples, and immediate feedback.",
        "steps": ["Learn the minimum theory needed.","Try a small task.","Observe the result.","Find and fix mistakes.","Increase difficulty gradually.","Build a small project or solve a new problem."],
        "best_for": "Programming, Computer Science, Maths practice, experiments, projects, and practical skills."
    }
}


# ==========================================
# SUBJECT-WISE STUDY TIPS
# ==========================================

SUBJECT_TIPS = {
    "maths": {
        "tips": [
            "Understand the concept before memorising formulas.",
            "Solve a mix of easy, medium, and challenging questions.",
            "Write every important step neatly.",
            "Always check your final answer and units.",
            "Practice previous years' questions and sample papers.",
            "Keep an error log of questions you got wrong.",
            "Revise formulas separately, then practise applying them.",
            "Draw a diagram whenever a geometry problem becomes confusing.",
            "Do not look at the solution too early; struggle productively first.",
            "Practise timed sets so calculation speed improves naturally.",
            "After solving, ask why the method works rather than only checking the answer."
        ],
        "recommended_method": "interleaving"
    },
    "science": {
        "tips": [
            "Draw labelled diagrams.",
            "Understand the 'why' behind every concept.",
            "Revise formulas, units, laws, and definitions regularly.",
            "Make short notes after every chapter.",
            "Relate concepts to daily life.",
            "Use active recall instead of repeatedly reading.",
            "Practise numericals separately from theory.",
            "Memorise chemical equations only after understanding the reaction.",
            "For Biology, connect structures with functions.",
            "For Physics, track units and sign conventions carefully.",
            "For Chemistry, learn patterns and reasons instead of isolated facts."
        ],
        "recommended_method": "active_recall"
    },
    "social science": {
        "tips": [
            "Prepare timelines for History.",
            "Use maps regularly for Geography.",
            "Connect Civics with real-life examples.",
            "Revise dates and terms using flashcards.",
            "Practice writing long answers with headings and keywords.",
            "Turn long paragraphs into short bullet points before memorising.",
            "Compare similar events, policies, regions, or concepts in a table.",
            "Practise map work frequently rather than once before the exam.",
            "Use cause → event → impact chains for History.",
            "For Economics, connect definitions to everyday examples."
        ],
        "recommended_method": "active_recall"
    },
    "english": {
        "tips": [
            "Read for at least 15-20 minutes every day.",
            "Improve vocabulary by learning useful words in context.",
            "Practise grammar exercises and review your errors.",
            "Write answers in your own words.",
            "Revise important literary devices with examples.",
            "For literature, remember theme, character, evidence, and message.",
            "Plan long answers before writing them.",
            "Use precise words instead of unnecessarily complicated vocabulary.",
            "Read your writing once for grammar and once for clarity.",
            "Practise notice, letter, article, report, and analytical writing formats if required."
        ],
        "recommended_method": "active_recall"
    },
    "computer": {
        "tips": [
            "Understand the logic instead of memorising code.",
            "Write small programs regularly.",
            "Debug your own code before checking a solution.",
            "Practise tracing programs line by line.",
            "Experiment with new ideas.",
            "Learn what each variable and function represents.",
            "Test edge cases and unexpected inputs.",
            "Break large problems into smaller functions.",
            "Read error messages carefully instead of guessing.",
            "Build tiny projects to turn concepts into practical skills."
        ],
        "recommended_method": "learning_by_doing"
    }
}


# ==========================================
# CAREER DATABASE
# ==========================================

CAREERS = {
    "maths": [
        "Data Scientist","Software Engineer","Data Analyst","AI/ML Engineer","Civil Engineer","Mechanical Engineer","Electrical Engineer","Electronics Engineer","Statistician","Actuary","Economist","Quantitative Analyst","Research Scientist","Astronomer","Architect","Robotics Engineer","Game Developer","Cybersecurity Engineer","Operations Research Analyst"
    ],
    "science": [
        "Doctor","Scientist","Pharmacist","Biotechnologist","Environmental Scientist","Forensic Expert","Physiotherapist","Dentist","Veterinarian","Microbiologist","Neuroscientist","Geneticist","Chemist","Physicist","Astronomer","Biomedical Engineer","Nutrition Scientist","Geologist","Marine Biologist"
    ],
    "commerce": [
        "Chartered Accountant","Financial Analyst","Investment Banker","Business Consultant","Entrepreneur","Economist","Company Secretary","Cost Accountant","Auditor","Actuary","Marketing Analyst","Business Analyst","Product Manager","Human Resources Specialist","Banking Professional","Financial Planner","Tax Consultant","E-commerce Manager"
    ],
    "humanities": [
        "Lawyer","Journalist","Psychologist","Civil Services","Teacher","Professor","Historian","Political Scientist","Sociologist","Economist","Writer","Editor","Content Strategist","Graphic Designer","UX Designer","Public Relations Specialist","International Relations Specialist","Social Worker","Archaeologist","Language Specialist"
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
    "You don't have to be the smartest. Just don't stop learning.",
    "A difficult chapter is not a verdict on your ability.",
    "You can be confused today and understand it tomorrow.",
    "One bad test does not define your ability.",
    "Start before you feel perfectly ready.",
    "Focus on the next useful step, not the entire mountain.",
    "Consistency turns small sessions into big progress.",
    "Questions are proof that you're trying to understand.",
    "Mistakes are information: use them to decide what to practise next.",
    "You don't need a perfect day to have a productive hour.",
    "Slow progress is still progress."
]


# ==========================================
# FUN FACTS
# ==========================================

FUN_FACTS = [
    "Your brain uses around 20% of your body's total energy.",
    "Octopuses have three hearts.",
    "Honey can remain edible for extremely long periods when properly sealed.",
    "Lightning can heat air to temperatures hotter than the Sun's surface.",
    "Bananas are botanically berries, while strawberries are aggregate fruits.",
    "A day on Venus is longer than its year.",
    "The Eiffel Tower expands slightly in hot weather because materials expand when heated.",
    "Sharks existed before trees in Earth's history.",
    "A group of flamingos is often called a flamboyance.",
    "Water is one of the few common substances naturally found as solid, liquid, and gas on Earth.",
    "Some bamboo species can grow extremely quickly under suitable conditions.",
    "The Moon is slowly moving farther away from Earth.",
    "Sound travels faster through water than through air.",
    "There are more possible chess games than atoms in the observable universe is a common comparison, illustrating how enormous the game tree is.",
    "The human body contains trillions of cells and many more microbes living on and in it."
]


# ==========================================
# HOMEWORK GUIDANCE
# ==========================================

HOMEWORK_GUIDE = {
    "maths": "Show every calculation step clearly before writing the final answer. State the formula, substitute values carefully, simplify, and check whether the result is reasonable.",
    "science": "Use diagrams wherever useful and explain the concept in simple language. Include laws, formulas, units, equations, labels, and key terms where relevant.",
    "english": "Answer in your own words instead of copying directly from the textbook. Follow the required format, use clear paragraphs, and check grammar and punctuation.",
    "social science": "Write answers in points with headings and important keywords. For History use causes/events/effects, for Geography use examples/maps, for Civics use concepts/examples, and for Economics connect ideas to real life.",
    "computer": "Explain the logic first and then write the program neatly. Test inputs, trace the code, read errors carefully, and mention the expected output when useful."
}


# ==========================================
# HELP MENU
# ==========================================

HELP_MENU = [
    "Study Tips","Time Management","Homework Help","Career Guidance","Motivational Quotes","Quiz","Maths Helper","General Knowledge","Fun Facts","Science Facts","Grammar Tips","Coding Tips","Study Methods","Daily Challenge","Formulas"
]


# Error Messages

ERROR_MESSAGES = [
    "Sorry, I couldn't understand that.",
    "Could you ask your question in a different way?",
    "I'm still learning about that topic.",
    "Please try using different keywords.",
    "I don't have enough information to answer that.",
    "Let's try another way of asking.",
    "Hmm... I couldn't figure that out.",
    "That doesn't seem familiar to me yet.",
    "I couldn't identify the subject. Try mentioning Maths, Science, English, Social Science, or Computer.",
    "I need a little more context. Tell me what you want to learn or solve.",
    "Try asking in a simple form such as 'quiz me on science' or 'give me maths tips'."
]


# Quiz Questions

QUIZ_QUESTIONS = {
    "maths": [
        {"question":"What is √144?","options":["10","12","14","16"],"answer":2},
        {"question":"What is 15 × 8?","options":["110","120","130","140"],"answer":2},
        {"question":"The value of π is closest to:","options":["2.14","3.14","4.13","3.41"],"answer":2},
        {"question":"How many degrees are there in a right angle?","options":["45","60","90","180"],"answer":3},
        {"question":"What is 9²?","options":["18","72","81","99"],"answer":3},
        {"question":"What is the perimeter of a square with side length 6?","options":["12","24","36","18"],"answer":2},
        {"question":"What is 2⁵?","options":["10","16","32","64"],"answer":3},
        {"question":"What is the smallest prime number?","options":["0","1","2","3"],"answer":3},
        {"question":"What is 15% of 200?","options":["20","25","30","35"],"answer":3},
        {"question":"The sum of angles in a triangle is:","options":["90°","180°","270°","360°"],"answer":2},
        {"question":"If 3x = 21, what is x?","options":["5","6","7","8"],"answer":3},
        {"question":"HCF of 18 and 24 is:","options":["3","6","9","12"],"answer":2},
        {"question":"LCM of 4 and 6 is:","options":["8","10","12","24"],"answer":3},
        {"question":"What is the area of a rectangle 8 cm long and 5 cm wide?","options":["13 cm²","26 cm²","40 cm²","80 cm²"],"answer":3},
        {"question":"What is the probability of getting heads on a fair coin?","options":["0","1/4","1/2","1"],"answer":3},
        {"question":"What is the mean of 2, 4, 6, 8?","options":["4","5","6","7"],"answer":2},
        {"question":"If x² = 49 and x is positive, x = ?","options":["5","6","7","8"],"answer":3},
        {"question":"What is 0.75 as a fraction in simplest form?","options":["1/2","2/3","3/4","4/5"],"answer":3},
        {"question":"A triangle with all three equal sides is called:","options":["Scalene","Isosceles","Right","Equilateral"],"answer":4},
        {"question":"What is the value of 5! ?","options":["20","60","100","120"],"answer":4}
    ],
    "science": [
        {"question":"What is the SI unit of Force?","options":["Joule","Newton","Pascal","Watt"],"answer":2},
        {"question":"Plants prepare food by:","options":["Respiration","Photosynthesis","Digestion","Fermentation"],"answer":2},
        {"question":"Which organ filters blood and forms urine?","options":["Heart","Kidney","Lungs","Stomach"],"answer":2},
        {"question":"The speed of light is approximately:","options":["3×10⁸ m/s","3000 m/s","300 m/s","3×10⁶ m/s"],"answer":1},
        {"question":"Which gas is most abundant in Earth's atmosphere?","options":["Oxygen","Nitrogen","Carbon dioxide","Hydrogen"],"answer":2},
        {"question":"Which element has the symbol O?","options":["Osmium","Gold","Oxygen","Oxide"],"answer":3},
        {"question":"Which organ pumps blood through the body?","options":["Lungs","Heart","Brain","Liver"],"answer":2},
        {"question":"What is the chemical formula of water?","options":["CO₂","H₂O","NaCl","O₂"],"answer":2},
        {"question":"The powerhouse of the cell is the:","options":["Nucleus","Ribosome","Mitochondrion","Chloroplast"],"answer":3},
        {"question":"Which planet is closest to the Sun?","options":["Venus","Earth","Mercury","Mars"],"answer":3},
        {"question":"Which process releases energy from food in cells?","options":["Respiration","Photosynthesis","Transpiration","Diffusion"],"answer":1},
        {"question":"A substance with pH less than 7 is generally:","options":["Acidic","Basic","Neutral","Metallic"],"answer":1},
        {"question":"What is the SI unit of electric current?","options":["Volt","Ampere","Ohm","Watt"],"answer":2},
        {"question":"Which force pulls objects toward Earth?","options":["Friction","Magnetism","Gravity","Buoyancy"],"answer":3},
        {"question":"What is the basic unit of life?","options":["Tissue","Organ","Cell","Atom"],"answer":3},
        {"question":"Which blood cells help fight infections?","options":["Red blood cells","White blood cells","Platelets","Plasma"],"answer":2},
        {"question":"What happens to most substances when heated?","options":["They always shrink","They generally expand","They disappear","They become weightless"],"answer":2},
        {"question":"Which part of a plant absorbs most water from soil?","options":["Flower","Root","Fruit","Leaf"],"answer":2},
        {"question":"Which metal is liquid at room temperature?","options":["Iron","Copper","Mercury","Aluminium"],"answer":3},
        {"question":"What is the SI unit of energy?","options":["Newton","Joule","Pascal","Watt"],"answer":2}
    ],
    "computer": [
        {"question":"CPU stands for:","options":["Central Processing Unit","Computer Primary Unit","Central Program Unit","Computer Processing Utility"],"answer":1},
        {"question":"Python is a:","options":["Programming Language","Browser","Database","Operating System"],"answer":1},
        {"question":"Which symbol starts a comment in Python?","options":["//","#","<!--","*"],"answer":2},
        {"question":"Which loop repeats while a condition is True?","options":["for","repeat","while","loop"],"answer":3},
        {"question":"Which function takes user input in Python?","options":["print()","input()","type()","read()"],"answer":2},
        {"question":"RAM stands for:","options":["Read Access Memory","Random Access Memory","Rapid Action Module","Remote Access Machine"],"answer":2},
        {"question":"Which storage retains data without power?","options":["RAM","Cache","ROM","Registers"],"answer":3},
        {"question":"1 Byte consists of how many bits?","options":["4","8","16","32"],"answer":2},
        {"question":"Which keyword defines a function in Python?","options":["function","def","func","define"],"answer":2},
        {"question":"HTML is mainly used for creating:","options":["Databases","Web pages","Operating systems","Compilers"],"answer":2},
        {"question":"Which Python data type stores an ordered mutable collection?","options":["tuple","list","set","int"],"answer":2},
        {"question":"Which operator checks equality in Python?","options":["=","==","!=","=>"],"answer":2},
        {"question":"What does len() return for a string?","options":["Its last character","Its number of characters","Its data type","Its memory address"],"answer":2},
        {"question":"Which statement is used to make a decision in Python?","options":["if","loop","caseonly","choose"],"answer":1},
        {"question":"Which value represents False in Python?","options":["1","True","False","yes"],"answer":3},
        {"question":"Which symbol is used for exponentiation in Python?","options":["^","**","//","%%"],"answer":2},
        {"question":"What is an algorithm?","options":["A step-by-step procedure for solving a problem","A computer cable","A storage device","A programming font"],"answer":1},
        {"question":"What does debugging mean?","options":["Deleting all code","Finding and fixing errors","Printing code","Encrypting a file"],"answer":2},
        {"question":"Which HTML tag creates a paragraph?","options":["<p>","<h1>","<br>","<img>"],"answer":1},
        {"question":"Which CSS property changes text size?","options":["font-size","text-color","size-text","font-height-only"],"answer":1}
    ],
    "general": [
        {"question":"Capital of India?","options":["Mumbai","Delhi","Kolkata","Chennai"],"answer":2},
        {"question":"How many continents are there?","options":["5","6","7","8"],"answer":3},
        {"question":"Which planet is called the Red Planet?","options":["Earth","Mars","Jupiter","Mercury"],"answer":2},
        {"question":"Largest ocean?","options":["Atlantic","Indian","Pacific","Arctic"],"answer":3},
        {"question":"National bird of India?","options":["Peacock","Parrot","Sparrow","Crow"],"answer":1},
        {"question":"How many colours are traditionally listed in a rainbow?","options":["5","6","7","8"],"answer":3},
        {"question":"Who wrote the national anthem of India?","options":["Rabindranath Tagore","Bankim Chandra Chatterjee","Sarojini Naidu","Mahatma Gandhi"],"answer":1},
        {"question":"Smallest Indian state by area?","options":["Sikkim","Goa","Tripura","Mizoram"],"answer":2},
        {"question":"Which is commonly recognized as the longest river in the world?","options":["Amazon","Nile","Ganga","Mississippi"],"answer":2},
        {"question":"How many days are in a leap year?","options":["365","366","364","367"],"answer":2},
        {"question":"Which is the largest planet in our Solar System?","options":["Earth","Saturn","Jupiter","Neptune"],"answer":3},
        {"question":"Which country is known as the Land of the Rising Sun?","options":["China","Japan","Thailand","Korea"],"answer":2},
        {"question":"What is the currency of India?","options":["Rupee","Yen","Dollar","Pound"],"answer":1},
        {"question":"Which is the largest continent by area?","options":["Africa","Europe","Asia","North America"],"answer":3},
        {"question":"How many players are on the field for one cricket team at a time?","options":["9","10","11","12"],"answer":3},
        {"question":"Which gas do humans need for aerobic respiration?","options":["Nitrogen","Oxygen","Helium","Carbon dioxide"],"answer":2},
        {"question":"What is the hardest natural substance commonly known?","options":["Iron","Quartz","Diamond","Granite"],"answer":3},
        {"question":"Which instrument measures temperature?","options":["Barometer","Thermometer","Ammeter","Hygrometer"],"answer":2},
        {"question":"How many sides does a hexagon have?","options":["5","6","7","8"],"answer":2},
        {"question":"Which ocean lies between Africa, Asia and Australia?","options":["Atlantic","Indian","Pacific","Arctic"],"answer":2}
    ]
}


# Formula Database

FORMULAS = {
    "area_circle":{"formula":"π × r²","variables":"r = radius","chapter":"Mensuration","class":"9"},
    "circumference":{"formula":"2 × π × r","variables":"r = radius","chapter":"Mensuration","class":"9"},
    "area_rectangle":{"formula":"length × breadth","variables":"l = length, b = breadth","chapter":"Mensuration","class":"9"},
    "area_square":{"formula":"side²","variables":"side = length of one side","chapter":"Mensuration","class":"9"},
    "pythagoras":{"formula":"a² + b² = c²","variables":"c = hypotenuse","chapter":"Triangles","class":"9"},
    "speed":{"formula":"Distance / Time","variables":"S = Speed","chapter":"Motion","class":"9"},
    "density":{"formula":"Mass / Volume","variables":"D = Density","chapter":"Matter","class":"9"},
    "force":{"formula":"Mass × Acceleration","variables":"F = Force","chapter":"Force and Laws of Motion","class":"9"},
    "work":{"formula":"Force × Displacement","variables":"W = Work","chapter":"Work and Energy","class":"9"},
    "power":{"formula":"Work / Time","variables":"P = Power","chapter":"Work and Energy","class":"9"},
    "kinetic_energy":{"formula":"½ × m × v²","variables":"m = mass, v = velocity","chapter":"Work and Energy","class":"9"},
    "potential_energy":{"formula":"m × g × h","variables":"m = mass, g = acceleration due to gravity, h = height","chapter":"Work and Energy","class":"9"},
    "momentum":{"formula":"m × v","variables":"m = mass, v = velocity","chapter":"Force and Laws of Motion","class":"9"},
    "average_speed":{"formula":"Total Distance / Total Time","variables":"distance and time must use compatible units","chapter":"Motion","class":"9"},
    "frequency":{"formula":"Number of oscillations / Time","variables":"f = frequency","chapter":"Sound","class":"9"},
    "area_triangle":{"formula":"½ × base × height","variables":"b = base, h = perpendicular height","chapter":"Heron's Formula / Geometry","class":"9"},
    "heron":{"formula":"√[s(s-a)(s-b)(s-c)]","variables":"s = (a+b+c)/2","chapter":"Heron's Formula","class":"9"},
    "linear_equation":{"formula":"ax + b = 0 → x = -b/a","variables":"a ≠ 0","chapter":"Algebra","class":"9"},
    "percentage":{"formula":"(Part / Whole) × 100","variables":"Part = required portion, Whole = total","chapter":"Number Systems / Arithmetic","class":"9"},
    "simple_interest":{"formula":"(P × R × T) / 100","variables":"P = principal, R = rate %, T = time","chapter":"Commercial Arithmetic","class":"9"},
    "compound_interest":{"formula":"P(1 + R/100)^T - P","variables":"P = principal, R = rate %, T = time","chapter":"Commercial Arithmetic","class":"9"},
    "trigonometric_basic":{"formula":"sin θ = perpendicular/hypotenuse; cos θ = base/hypotenuse; tan θ = perpendicular/base","variables":"right-angled triangle","chapter":"Trigonometry","class":"10"},
    "quadratic_formula":{"formula":"x = (-b ± √(b² - 4ac)) / 2a","variables":"ax² + bx + c = 0","chapter":"Quadratic Equations","class":"10"}
}


# Science Facts

SCIENCE_FACTS = [
    "The human brain contains roughly 86 billion neurons.",
    "Sound cannot travel through a vacuum.",
    "Lightning can heat surrounding air to temperatures hotter than the Sun's surface.",
    "Water expands when it freezes, making ice less dense than liquid water.",
    "Earth takes about 365.25 days to orbit the Sun.",
    "DNA stands for Deoxyribonucleic Acid.",
    "Plants release oxygen as a product of photosynthesis.",
    "The speed of light in vacuum is approximately 3 × 10⁸ m/s.",
    "Gravity on the Moon is about one-sixth of Earth's surface gravity.",
    "The SI unit of energy is the joule.",
    "The SI unit of electric current is the ampere.",
    "Mitochondria are major sites of aerobic cellular respiration.",
    "Red blood cells contain haemoglobin, which helps transport oxygen.",
    "The ozone layer absorbs much of the Sun's harmful ultraviolet radiation.",
    "A balanced chemical equation has equal numbers of each type of atom on both sides.",
    "Plants lose water vapour mainly through a process called transpiration.",
    "Friction can be useful, such as when walking or braking.",
    "Pressure is force acting per unit area.",
    "A convex lens can converge parallel rays of light.",
    "The nucleus contains most of a cell's genetic material in eukaryotic cells."
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
    "Check subject-verb agreement.",
    "Use 'its' for possession and 'it's' for 'it is' or 'it has'.",
    "Use 'your' for possession and 'you're' for 'you are'.",
    "Affect is usually a verb; effect is usually a noun, though context matters.",
    "Use a comma to separate items in a list.",
    "Do not join two independent sentences with only a comma.",
    "Keep verb tense consistent unless there is a reason to change it.",
    "Use articles a/an/the appropriately.",
    "Avoid sentence fragments in formal writing.",
    "Match pronouns clearly to the nouns they refer to.",
    "Prefer clear, precise wording over unnecessarily complicated sentences.",
    "Check spelling of commonly confused words before submitting.",
    "For formal answers, avoid excessive slang and texting abbreviations."
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
    "Avoid repeating the same code.",
    "Start debugging by reproducing the problem consistently.",
    "Change one thing at a time while debugging.",
    "Use print statements or a debugger to inspect unexpected values.",
    "Validate user input when your program expects a particular format.",
    "Use functions to separate reusable logic.",
    "Choose the simplest data structure that fits the problem.",
    "Handle edge cases such as empty input, zero, negative values, or very large values.",
    "Name constants clearly and avoid unexplained magic numbers.",
    "Read documentation before guessing how an API works.",
    "Test small pieces before combining them into a large program.",
    "Keep code formatting consistent.",
    "If a bug is confusing, reduce the program to the smallest example that still fails."
]


# Daily Challenges

DAILY_CHALLENGES = [
    "Revise one Science chapter today.",
    "Solve 20 Maths questions.",
    "Read 10 pages of an English book.",
    "Learn 5 new vocabulary words and use each in a sentence.",
    "Practice Python for 30 minutes.",
    "Complete one pending homework task.",
    "Revise yesterday's class notes without looking first.",
    "Teach a concept to someone else.",
    "Make short notes of one chapter.",
    "Solve one previous year question paper or a timed section.",
    "Do a 25-minute distraction-free study session.",
    "Create 10 active-recall questions from today's lesson.",
    "Review the mistakes from your last test.",
    "Practise 5 Maths questions you previously got wrong.",
    "Draw and label one important Science diagram from memory.",
    "Make a mini timeline for one History chapter.",
    "Practise one writing format in English.",
    "Build a tiny Python program using today's concept.",
    "Learn one new formula and solve two examples using it.",
    "Organise your notes and remove duplicate or outdated material.",
    "Spend 15 minutes revising vocabulary or definitions.",
    "Explain one difficult concept aloud without reading notes.",
    "Do one mixed-topic Maths practice set.",
    "Finish one task you have been postponing."
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
    "Help me with homework.",
    "Quiz me on Maths.",
    "Quiz me on Science.",
    "Quiz me on Computer Science.",
    "Give me a General Knowledge quiz.",
    "Teach me active recall.",
    "How do I stop procrastinating?",
    "How should I revise before an exam?",
    "Give me a study method.",
    "Explain a formula.",
    "Give me an English grammar tip."
]


# Achievement Messages

ACHIEVEMENTS = {
    "first_chat":"🎉 Congratulations! You've started your StudyBuddy journey.",
    "first_quiz":"🏅 Great! You completed your first quiz.",
    "five_quizzes":"🥈 Quiz Explorer - Completed 5 quizzes!",
    "ten_quizzes":"🥇 Quiz Champion - Completed 10 quizzes!",
    "perfect_score":"🌟 Excellent! You scored full marks!",
    "study_streak_3":"🔥 3-Day Study Streak!",
    "study_streak_7":"🔥 Incredible! 7-Day Study Streak!",
    "study_streak_30":"🏆 Amazing! 30-Day Study Streak!",
    "ten_questions":"📚 Practice Builder - Answered 10 quiz questions!",
    "fifty_questions":"🎓 Knowledge Grinder - Answered 50 quiz questions!",
    "first_homework":"✏️ Homework Hero - Completed your first homework-help session!",
    "first_formula":"🧮 Formula Finder - Looked up your first formula!",
    "first_challenge":"⚡ Challenge Accepted - Completed your first daily challenge!"
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
    "Today's effort becomes tomorrow's success.",
    "You do not need to finish everything at once; start with one task.",
    "If you got something wrong, now you know exactly what to practise.",
    "Take a breath, simplify the problem, and try the next step.",
    "A focused 20 minutes is better than an hour of distracted studying.",
    "Don't compare your chapter one to someone else's chapter ten.",
    "Ask questions whenever something doesn't make sense.",
    "You are allowed to learn slowly as long as you keep moving.",
    "Your mistakes can become your revision list.",
    "One difficult question does not mean you cannot learn the topic.",
    "Keep showing up."
]


# Success Messages

SUCCESS_MESSAGES = [
    "Great job! ✅","Excellent work! 🌟","Well done! 🎉","That's correct! 👏","Fantastic! Keep it up!","You're doing really well!","Nice work!","Brilliant answer!","Perfect! 💯","Nailed it! 🔥","Correct! Keep going.","That's it!","Great reasoning!","Strong answer!","You got it! 🎯"
]


# Help Text

HELP_TEXT = """
Welcome to StudyBuddy!

You can ask things like:

• Hi
• Give me study tips
• Motivate me
• Start a Maths, Science, Computer, or General quiz
• Solve 25*36
• Find square root of 144
• Tell me a science fact
• Give me a coding tip
• Give me a grammar tip
• Help me with homework
• Suggest a career
• Show me a formula
• Give me a study method
• Make a study plan
• Give me today's challenge
• Help me manage my time

Type 'bye' anytime to exit.
"""


# Goodbye Messages

GOODBYE_QUOTES = [
    "Keep learning. See you soon!",
    "Have a productive day!",
    "Stay curious and keep growing.",
    "Good luck with your studies!",
    "Learning never stops. Goodbye!",
    "See you next study session! 📚",
    "Take care and keep asking questions.",
    "Bye! One small step today can make tomorrow easier."
]