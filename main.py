import sys
import os 
import argparse 
import random
from knapsack import Knapsack, Item

parser=argparse.ArgumentParser()
parser.add_argument("-dynamic", action="store_true" , help="Dynamic solution")
parser.add_argument("-bruteforce", action="store_true" , help="Bruteforce solution")
args = parser.parse_args()




if __name__ == "__main__":
    items = []
    for i in range(6):# 6 bo 6 itemkow mamy
        value, weight = map(int, input("Enter value and weight: ").split())
        name = input("Enter name of the item: ")
        capacity = input("Enter capacity: ")
        items.append(Item(value, weight, name))

    knapsack = Knapsack(capacity, items)
    knapsack.solve()
    knapsack.display_results()
    knapsack.calculate_items()