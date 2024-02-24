def closest_to_center(x1, y1, x2, y2):
    distance1 = x1 ** 2 + y1 ** 2
    distance2 = x2 ** 2 + y2 ** 2

    if distance1 <= distance2:
        return x1, y1
    else:
        return x2, y2


def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    x_closest_1, y_closest_1 = closest_to_center(x1, y1, x2, y2)
    x_closest_2, y_closest_2 = closest_to_center(x3, y3, x4, y4)

    distance1 = calculate_distance(x_closest_1, y_closest_1, 0, 0)
    distance2 = calculate_distance(x_closest_2, y_closest_2, 0, 0)

    line1_length = calculate_distance(x1, y1, x2, y2)
    line2_length = calculate_distance(x3, y3, x4, y4)

    if line1_length >= line2_length:
        print(f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})")
    else:
        print(f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
