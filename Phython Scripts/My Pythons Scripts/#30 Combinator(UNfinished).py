# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:15:10 2024

@author: david
"""

# Define your list of lists
lists = [['a', 'b', 'c'], [1, 2, 3], ['x', 'y', 'z']]

# Initialize an empty list to store the combinations
combinations = [[]]

# Use nested for loops to generate all combinations
for sublist in lists:
    new_combinations = []
    for combination in combinations:
        for item in sublist:
            new_combinations.append(combination + [item])
    combinations = new_combinations

# Print the combinations
for combination in combinations:
    print(combination)
