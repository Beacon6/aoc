#!/usr/bin/env python

def calculate_distance(path):
    with open(path, "r") as file:
        lines = file.readlines()

    list_a, list_b = [], []

    for line in lines:
        split_line = line.split("   ")
        list_a.append(split_line[0])
        list_b.append(split_line[1].strip())

    list_a.sort()
    list_b.sort()

    distances = []
    length = len(list_a)

    for i in range(length):
        distances.append(abs(int(list_a[i]) - int(list_b[i])))

    return sum(distances)

res = calculate_distance("day_1.txt")
print(res)
