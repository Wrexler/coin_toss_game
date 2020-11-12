import numpy as np

results = []

for turn in range(10):
    print("Toss the coin Yes/(No)... ")
    prompt = input()
    if prompt == "Yes":
        coin = np.random.randint(0,2)
        if coin == 0:
            print("Heads")
            results.append("Heads")
        else:
            print("Tails")
            results.append("Tails")
    else:
        print("Game Over")
        print(results)
        break