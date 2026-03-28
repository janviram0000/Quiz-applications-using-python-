def run_quiz():
    questions = [
        {"prompt": "What is the capital of France?", "answer": "Paris"},
        {"prompt": "Which language is used for Python?", "answer": "Python"},
        {"prompt": "What is 10 + 5?", "answer": "15"},
        {"prompt": "Is Python a snake? (Yes/No)", "answer": "Yes"}
    ]

    score = 0
    print("--- Welcome to the Quiz! ---")

    for q in questions:
        user_answer = input(f"\n{q['prompt']} ")
        if user_answer.lower() == q['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nQuiz Over! Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
  
