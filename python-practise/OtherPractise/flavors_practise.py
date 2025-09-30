flavors = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

second_flavor = []
start = 0
while start < 6:
    start += 1 
    for i in flavors[start: ]:
        second_flavor.append(i)

print(second_flavor)

for a in second_flavor[ : 6]:
    print(f"Banana, {a}")

for b in second_flavor[6 : 11]:
    print(f"Chocolate, {b}")

for c in second_flavor[11 : 15]:
    print(f"Lemon, {c}")

for d in second_flavor[15 : 18]:
    print(f"Pistachio, {d}")

for e in second_flavor[18 : 20]:
    print(f"Raspberry, {e}")

for f in second_flavor[20: 21]:
    print(f"Strawberry, {f}")


#code someone else wrote. How does is flavor1 < flavor2??

""" for flavor1 in flavors:
    for flavor2 in flavors:
        if flavor1 < flavor2:
            print(flavor1 + ", " + flavor2) """