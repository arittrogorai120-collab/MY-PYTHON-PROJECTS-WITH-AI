import random 

number = random.randint(1, 100)

attempts=  0

while True:
    guess = int(input("enter your no"))
    attempts +=1

    print("welcome to the guessing game . if you correctly guss you will win 100 per guess")

    if guess > number:
        print("printlower number please")

    elif guess < number:
        print("print higher number please")

    else:
        print(f"you guessed the correct number in {attempts} attempts ")
        break