## Quiz App Program using File Handling

FILE_NAME = "quiz.txt"

# Load questions from file
def load_questions():
    questions = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 6:
                    question = {
                        "q": parts[0],
                        "options": parts[1:5],
                        "answer": parts[5]
                    }
                    questions.append(question)
    except FileNotFoundError:
        print("Quiz file not found!")
    return questions

# Run quiz
def run_quiz(questions):
    score = 0
    
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['q']}")
        
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")
        
        choice = input("Enter option number: ")
        
        if q['options'][int(choice)-1] == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {q['answer']}")
    
    print(f"\nYour Score: {score}/{len(questions)}")

# Main
def main():
    questions = load_questions()
    
    if questions:
        run_quiz(questions)
    else:
        print("No questions available.")

# Run program
main()
