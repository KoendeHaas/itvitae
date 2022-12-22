""" Quiz tool"""
import json
import random

with open("questions.json", encoding='UTF-8') as questions:
    questions = json.load(questions)
    random.shuffle(questions)

    print("Welcome to quizerr\n")

    for question in questions:
        print(f'{question["question"]}\n')
        print(f'A: {question["A"]}')
        print(f'B: {question["B"]}')
        print(f'C: {question["C"]}')
        print(f'D: {question["D"]}')

        user_input = input("\nAnswer: ").upper()

        if user_input != question["correct"]:
            print(f"\nIncorrect: the correct answer was: {question['correct']}\n")
        else:
            print("\ncorrect!\n")
