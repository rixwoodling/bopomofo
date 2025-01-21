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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 flashcards.py bopomofo.csv")
        return

    file_path = sys.argv[1]
    try:
        data = load_csv(file_path)
        if not data:
            return

        while True:
            clear_screen()
            item = random.choice(data)
            print(item[0])
            input()
            print(item[1])
            input()

    except Exception:
        return

if __name__ == "__main__":
    main()
