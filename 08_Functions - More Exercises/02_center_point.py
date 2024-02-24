def closest_to_center(x1, y1, x2, y2):
    distance1 = abs(x1) ** 2 + abs(y1) ** 2
    distance2 = abs(x2) ** 2 + abs(y2) ** 2

    if distance1 <= distance2:
        print(f"({int(x1)}, {int(y1)})")
    else:
        print(f"({int(x2)}, {int(y2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

closest_to_center(x1, y1, x2, y2)
