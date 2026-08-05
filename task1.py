import random

posture = random.choice(["sitting", "standing"])
direction = random.choice(["left", "right", "facing"])
distance = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"Start State -> Posture: {posture}, Direction: {direction}, Distance:{distance}")

if posture == "sitting":
    print("Nexus stands up")
    posture = "standing"
if direction != "facing":
    if direction == "left":
        print("Nexus turn toward the door")
        direction = "facing"
    elif direction == "right":
        print("Nexus turn toward the door")
        direction = "facing"
for i in range(1,11):
    if i < distance:
        print(f"Moving... {distance-i} steps left")
    if i == distance:
        print("distance is zero")
        break