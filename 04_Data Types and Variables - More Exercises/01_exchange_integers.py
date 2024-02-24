a = int(input())
b = int(input())
print("Before:")
print(f"a = {a}")
print(f"b = {b}")
saved_a = a
a = b
b = saved_a
print("After:")
print(f"a = {a}")
print(f"b = {b}")
