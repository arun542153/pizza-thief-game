import random

print("😂 WELCOME TO THE FUNNY GAME 😂")
print("A thief has stolen your pizza! 🍕")
print("Catch the thief to get your pizza back!")

secret_number = random.randint(1, 10)
attempts = 3
caught = False

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("😂 YOU CAUGHT THE THIEF!")
        print("🍕 Your pizza is safe!")
        caught = True
        break

    elif guess < secret_number:
        print("🤣 Wrong! The thief is hiding at a higher number!")

    else:
        print("😜 Wrong! Try a lower number!")

    attempts = attempts - 1

    if attempts > 0:
        print("Chances remaining:", attempts)

if not caught:
    print("💨 HAHAHA! The thief escaped!")
    print("🍕 Your pizza is gone!")
    print("The secret number was:", secret_number)

print("😂 GAME OVER! THANKS FOR PLAYING!")