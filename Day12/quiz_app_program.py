## Quiz App Program

# quiz data
questions = {
    "What is the capital of Japan?": {
        "options": ["A. Tokyo", "B. Seoul", "C. Beijing", "D. Bangkok"],
        "ans": "A"
    },
    "Which planet is called the Red Planet?": {
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "ans": "B"
    },
    "Who wrote Romeo and Juliet?": {
        "options": ["A. Dickens", "B. Shakespeare", "C. Twain", "D. Austen"],
        "ans": "B"
    },
    "Which country hosted 2016 Olympics?": {
        "options": ["A. China", "B. UK", "C. Brazil", "D. Russia"],
        "ans": "C"
    },
    "Largest ocean in the world?": {
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "ans": "C"
    }
}

score = 0

print("Welcome to my Quiz App ")
print("--------------------------")

# no shuffle, normal order
for q in questions:
    print("\n" + q)
    
    
    for op in questions[q]["options"]:
        print(op)
    
    user = input("Enter your answer: ").upper()

    if user == questions[q]["ans"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer")
        print("Correct was:", questions[q]["ans"])

print("\nQuiz Over!")
print("Your score is:", score, "/", len(questions))

# result message
if score == len(questions):
    print("Excellent!!!")
elif score >= 3:
    print("Good try...")
else:
    print("Keep practicing")
