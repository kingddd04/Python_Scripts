def roll_dice(current_combination, dice_left):
    if dice_left == 0:
        print(current_combination)
    else:
        for face in range(1, 7):
            roll_dice(current_combination + [face], dice_left - 1)

# Start the recursion with an empty combination and 3 dice to roll
roll_dice([], 2)