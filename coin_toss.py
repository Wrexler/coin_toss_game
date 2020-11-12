import numpy as np

results = []

for turn in range(100):
    print("Toss the coin Yes/(No)... ")
    prompt = input()
    if prompt == "Yes" or "yes" or "Y" or "y":
        coin = np.random.randint(0,2)
        if coin == 0:
            print("Heads")
            results.append("Heads")
        else:
            print("Tails")
            results.append("Tails")
    elif prompt == "No" or "no" or "N" or "n":
        print("Game Over")
        print(results)
        break
    else:
        print("Please choose either Yes or No to start coin toss...")
        prompt = input()