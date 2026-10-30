import random as r
questions = [
    {
        "question": "Which function generates a random integer?",
        "options": ["random()", "randint()", "choice()", "shuffle()"],

    },
    {
        "question": "What is the output of math.ceil(4.2)?",
        "options": ["4", "4.2", "5", "6"],
    },
    {
        "question": "Which function selects multiple elements without repetition?",
        "options": ["choice()", "choices()", "sample()", "shuffle()"],
    },
    {
        "question": "What does sys.getsizeof() return?",
        "options": ["Number of elements", "Memory size in bytes", "Python version", "File location"],
    },
    {
        "question": "Which statement immediately stops a loop?",
        "options": ["continue", "pass", "return", "break"],
        
    }
]
r.shuffle(questions)
for i in questions:
    print(i["question"])    
    for j in i["options"]:
            print(j)