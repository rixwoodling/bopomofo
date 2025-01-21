import csv
import random
import os
import sys

def clear_screen():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def load_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first line
        return list(reader)

def generate_choices(correct, all_items):
    # Ensure the correct answer is included among the choices
    choices = [correct]
    while len(choices) < 3:
        random_choice = random.choice(all_items)
        if random_choice != correct and random_choice not in choices:
            choices.append(random_choice)
    random.shuffle(choices)
    return choices

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 multiplechoice.py bopomofo.csv")
        return

    file_path = sys.argv[1]
    try:
        data = load_csv(file_path)
        if not data:
            return

        while True:
            clear_screen()
            item = random.choice(data)
            question, correct_answer = random.choice([(item[0], item[1]), (item[1], item[0])])

            # Generate multiple-choice options
            all_items = [row[0] for row in data] + [row[1] for row in data]
            choices = generate_choices(correct_answer, all_items)

            print(question)
            for idx, choice in enumerate(choices, start=1):
                print(f"{idx}. {choice}")

            user_input = input("Your answer: ")
            try:
                user_choice = int(user_input)
                if 1 <= user_choice <= 3:
                    if choices[user_choice - 1] == correct_answer:
                        print("Correct!")
                    else:
                        print("Incorrect!")
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

            input("Press Enter for the next question...")

    except Exception:
        return

if __name__ == "__main__":
    main()


