trucks = 50
capacity = 100
distance = 0
F = 1
while trucks > 0:
    distance += capacity / (trucks // F)
    # print(capacity // (trucks // F), distance, trucks)
    trucks = trucks - F
    print(distance, trucks, F)

print(trucks)
