import random
num = random.randint(1,100)
while True:
    guess=int(input("Guess number 1-100: "))
    if guess==num: print("Correct!"); break
    elif guess<num: print("Too low")
    else: print("Too high")
