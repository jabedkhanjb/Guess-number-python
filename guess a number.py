print("*" * 40)
print("          Guessing number Game")
print("*" * 40)
import random
secret_number = random.randint(1, 9)
#print(secret_number)
#int(input("Enter your secret number: "))
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")
    print(f"Your secret number was {secret_number}")
    print("\nVisit me: https://allmylinks.com/jabedkhanjb\nSupport team")