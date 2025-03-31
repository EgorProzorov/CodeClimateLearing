import math
import random


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    print("Find the smallest common multiple of given numbers.")
    play_lcm_game(name)

    print("What number is missing in the progression?")
    play_geometric_progression_game(name)


def play_lcm_game(name):
    for _ in range(3):
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = lcm(numbers[0], lcm(numbers[1], numbers[2]))

        print(f"Question: {' '.join(map(str, numbers))}")
        answer = input("Your answer: ")

        if answer.isdigit() and int(answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def play_geometric_progression_game(name):
    for _ in range(3):
        start = random.randint(1, 10)
        ratio = random.randint(2, 5)
        length = 10
        progression = [start * (ratio ** i) for i in range(length)]
        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = ".."

        print(f"Question: {' '.join(map(str, progression))}")
        answer = input("Your answer: ")

        if answer.isdigit() and int(answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()