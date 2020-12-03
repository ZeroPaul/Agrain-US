import operator
import collections

a = {'coated grain': 0.54241544, 'whole grain': 0.85758456, 'f':100, 'd': 12}

r = max(a.values())

sorted_x = sorted(a.items(), key=lambda x: x[1], reverse=True)
print(sorted_x[0][0], sorted_x[0][1])
