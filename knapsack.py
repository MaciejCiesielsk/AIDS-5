class Item:
    def __init__(self, value, weight, name):
        self.value = value
        self.weight = weight
        self.name = name

class Knapsack:
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items
        self.num_items = len(items)
        self.tabP = [[0] * (self.num_items + 1) for _ in range(self.capacity + 1)]
        self.tabQ = [[0] * (self.num_items + 1) for _ in range(self.capacity + 1)]

    def solve(self):
        for i in range(1, self.capacity + 1):
            for j in range(1, self.num_items + 1):
                current_item = self.items[j-1]
                if current_item.weight <= i and self.tabP[i][j-1] < (self.tabP[i-current_item.weight][j] + current_item.value):
                    self.tabP[i][j] = self.tabP[i-current_item.weight][j] + current_item.value
                    self.tabQ[i][j] = j
                else:
                    self.tabP[i][j] = self.tabP[i][j-1]
                    self.tabQ[i][j] = self.tabQ[i][j-1]

    def display_results(self):
        print("tabP table:")
        for row in self.tabP:
            for value in row:
                if value >= 10:
                    print(f"{value} ", end='')
                else:
                    print(f"{value}  ", end='')
            print()
        print("\ntabQ table:")
        for row in self.tabQ:
            for value in row:
                print(f"{value} ", end='')
            print()
        print("\n\nMaximum value is:", self.tabP[self.capacity][self.num_items])

    def calculate_items(self):
        counter = [0] * self.num_items
        b = self.capacity
        c = self.num_items
        while b > 0 and c > 0:
            if self.tabQ[b][c] > 0:
                counter[self.tabQ[b][c] - 1] += 1
                b -= self.items[self.tabQ[b][c] - 1].weight
            else:
                c -= 1
        for i in range(self.num_items):
            print(f"Item {self.items[i].name} was used: {counter[i]} times")



