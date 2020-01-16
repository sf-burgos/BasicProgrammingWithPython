from sys import stdin
from itertools import combinations

t = int(stdin.readline().strip())

for t in range(t):
    dollars = int(stdin.readline().strip())
    total_flavors = int(stdin.readline().strip())  
    flavors_costs = stdin.readline().strip()
    flavors_costs = [int(x) for x in flavors_costs.split(' ')]
    flavors_combinations = combinations(flavors_costs, 2)
    for flavors_tuple in flavors_combinations:
        if ((flavors_tuple[0] + flavors_tuple[1]) == dollars):
            first_flavor = flavors_costs.index(flavors_tuple[0])
            second_flavor = flavors_costs.index(flavors_tuple[1],first_flavor + 1)
            print("{} {}".format(first_flavor + 1, second_flavor + 1))
            break
