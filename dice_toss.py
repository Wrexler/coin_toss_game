import numpy as np

results = []

for outcome in range(10):
    print("Roll the dice (Yes)/(No)... ")
    prompt = input()
    if prompt == "Yes":
        dice_1 = np.random.randint(1,7)
        dice_2 = np.random.randint(1,7)
        results.append(dice_1 + dice_2)
        if dice_1 == dice_2:
            print("Snake Eyes")
            print("You win the game")
            break
        print(dice_1,dice_2)
    else:
        print("Game Over")
        print(results)
        break
