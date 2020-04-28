import random, sys

def right_number(attempt, number):
    if number == 42:
        print("The answer to the ultimate question of life, the universe and everything is 42.")
    if attempt > 1:
        print("Congratulations, you've got it!")
        print(f"You won in {attempt + 1} attempts!")
    else:
        print("Congratulations! You got it on your first try!")
    sys.exit(1)

def game_loop():
    attempts = 0
    number = random.randint(1, 99)
    while True:
        try:
            input_att = input("What's your guess between 1 and 99?\n>> ")
            if input_att == "exit":
                sys.exit("Goodbye!")
            input_att = int(input_att)
        except (KeyboardInterrupt, EOFError):
            sys.exit("Goodbye!")
        except ValueError:
            print("That's not a number.")
        else:
            if input_att == number:
                right_number(attempts, number)
            elif input_att > number:
                print("Too high!")
            else:
                print("Too low!")
        attempts += 1

def main():
    print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number. Type 'exit' to end the game.\n\
Good luck!")
    game_loop()

if __name__ == "__main__":
    main()