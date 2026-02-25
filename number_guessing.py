import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True
print("python number guessing game")
print(f"guess the number between {lowest_num} and {highest_num}")

while is_running:
    guess=int(input("Enter a number: "))
    guesses+=1
    if guess==answer:
        print("You got it!")
        is_running=False
    elif guess<answer:
        print("Too low!")
    else:
        print("Too high!")
print(f"you got it in {guesses} guesses")