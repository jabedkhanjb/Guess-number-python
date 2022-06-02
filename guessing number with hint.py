import random
secret_number = random.randint(1, 9)
countdown = 0
guessing_limit = 3
print("*" * 40)
print("          Guessing number Game")
print("*" * 40)
while countdown < guessing_limit:
    guess = int(input("Guess: "))
    if guess < secret_number:
        print("Higher...")
    elif guess > secret_number:
        print("Lower...")
    countdown += 1
    if countdown == guessing_limit:
        print(f"Sorry, you failed!\nYour secret number was {secret_number}")

    if guess == secret_number:
        print("Congratulations, You guessed it! Secret number was ", secret_number)
        print(f"And it only took you {countdown} tries\n")
        break
print("Visit me: https://allmylinks.com/jabedkhanjb\nSupport team")