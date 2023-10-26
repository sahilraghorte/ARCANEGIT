import random

questions = [
    {
        "question": "What is the capital of France?",
        "correct_answer": "Paris",
        "incorrect_answers": ["Berlin", "Madrid", "Rome"]
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "correct_answer": "Mars",
        "incorrect_answers": ["Venus", "Jupiter", "Saturn"]
    },
    {
        "question": "What is 2 + 2?",
        "correct_answer": "4",
        "incorrect_answers": ["3", "5", "6"]
    }
]


def ask_question(question_dict):
    print(question_dict["question"])
    options = [question_dict["correct_answer"]] + \
        question_dict["incorrect_answers"]
    random.shuffle(options)

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_choice = int(input("Enter the number of your answer: ")) - 1
    if options[user_choice] == question_dict["correct_answer"]:
        return True
    else:
        return False


def calculate_score(questions_list):
    score = 0
    for question in questions_list:
        if ask_question(question):
            score += 1
        print()
    return score


if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    print("You will be presented with a series of questions. Choose the correct answer.")
    print("Let's begin!\n")

    user_score = calculate_score(questions)

    print(f"Game Over! Your total score is: {user_score}/{len(questions)}")
