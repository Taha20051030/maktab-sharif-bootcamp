import random
status = False
base = random.randint(1, 20)
for _ in range(5):
    print("Please enter a number between 1 and 100:20")
    inp = int(input())
    if base == inp:
        status = True
        print("Bravo, you won!")
        break
    elif base > inp:
        print("Your answer is smaller than the computer's value.")
    else:
        print("Your answer is bigger than the computer's value.")
if status == False:
    print("I'm sorry, you lost.")
    print(f"The number guessed by the computer was {base}.")
