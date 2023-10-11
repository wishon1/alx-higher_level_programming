#!/usr/bin/python3
"""
function that returns the weighted average of all
integers tuple (<score>, <weight>)
"""


def weight_average(my_list=[]):
    if not my_list:
        return 0
    # Initialize lists to store weights and weighted values
    weights = []
    weighted_values = []
    # Iterate through the items in the input list
    for item in my_list:
        value = item[0]
        weight = item[1]
        weighted_values.append(value * weight)
        weights.append(weight)

    # Calculate the weighted average
    weighted_sum = sum(weighted_values)
    weight_sum = sum(weights)
    weighted_avg = weighted_sum / weight_sum

    return weighted_avg
