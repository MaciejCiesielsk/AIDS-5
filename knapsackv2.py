import sys
import os 
import argparse 
import random

parser = argparse.ArgumentParser()
parser.add_argument("-dynamic", action="store_true", help="Dynamic solution")
parser.add_argument("-bruteforce", action="store_true", help="Bruteforce solution")
args = parser.parse_args()
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def read_input_file(file_path):
    with open(CURRENT_DIR + '/data.txt', 'r') as file:
        lines = file.readlines()
        knapsack_capacity = int(lines[0])
        num_items = int(lines[1])
        items = []
        for line in lines[2:]:
            item_profit, item_weight = map(int, line.split())
            items.append((item_profit, item_weight))
        return knapsack_capacity, num_items, items


def dynamic_knapsack(knapsack_capacity, num_items, items):
    dp = [[0] * (knapsack_capacity + 1) for _ in range(num_items + 1)]
    chosen_items = [[[] for _ in range(knapsack_capacity + 1)] for _ in range(num_items + 1)]
    for i in range(1, min(num_items, len(items)) + 1):
        for j in range(1, knapsack_capacity + 1):
            item_profit, item_weight = items[i - 1]
            if item_weight > j:
                dp[i][j] = dp[i - 1][j]
                chosen_items[i][j] = chosen_items[i - 1][j]
            else:
                if dp[i - 1][j] < dp[i - 1][j - item_weight] + item_profit:
                    dp[i][j] = dp[i - 1][j - item_weight] + item_profit
                    chosen_items[i][j] = chosen_items[i - 1][j - item_weight] + [i]
                else:
                    dp[i][j] = dp[i - 1][j]
                    chosen_items[i][j] = chosen_items[i - 1][j]
    return dp[num_items][knapsack_capacity], chosen_items[num_items][knapsack_capacity]


def brute_force_knapsack(knapsack_capacity, num_items, items):
    max_value = 0
    chosen_items = []
    for i in range(2 ** num_items):
        value = 0
        weight = 0
        current_items = []
        for j in range(num_items):
            if (i >> j) & 1:
                item_profit, item_weight = items[j]
                value += item_profit
                weight += item_weight
                current_items.append(j + 1)  
        if weight <= knapsack_capacity and value > max_value:
            max_value = value
            chosen_items = current_items
    return max_value, chosen_items  


if __name__ == "__main__":
    if args.dynamic:
        knapsack_capacity, num_items, items = read_input_file(CURRENT_DIR + '/data.txt') 
        dp_result, chosen_items = dynamic_knapsack(knapsack_capacity, num_items, items)
        print("Dynamic Programming Result:", dp_result)
        print("Chosen Items:", chosen_items)  
    elif args.bruteforce:
        knapsack_capacity, num_items, items = read_input_file(CURRENT_DIR + '/data.txt')
        bf_result, chosen_items = brute_force_knapsack(knapsack_capacity, num_items, items)
        print("Brute Force Result:", bf_result)
        print("Chosen Items:", chosen_items)  
    else:  
        print("Please use -dynamic or -bruteforce")
        sys.exit(1)
