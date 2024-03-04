import random

class DiceRoller:
    def __init__(self):
        pass

    def roll_dice(self):
        roll_dice = True
        while roll_dice:
            dice_choice = input("which dice would you like to roll? Type : 'd4','d6','d8','d10','d12','d20', r for return")
            if dice_choice == 'r':
                roll_dice = False
            elif dice_choice != 'r':
                number_dice_choice = int(dice_choice[1:])
                amount_dice = int(input("How many dice would you like to roll?"))
                for _ in range(amount_dice):
                    roll = random.randint(1, number_dice_choice)
                    print(f"{'*'*5}#{_+1}-{dice_choice}:{roll}{'*'*5}")

