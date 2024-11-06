import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess a Number between (1 - 100): "))
    if(a > n):
        print("Lower Number Please...")
    elif(a < n):
        print("Higher Number Please...")
    elif(a == n):
        print(f"Congratulations!!, You have Guessed the correct number {n} in {guesses} attempts.")
        break