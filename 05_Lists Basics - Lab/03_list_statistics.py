my_positive_list = []
my_negative_list = []
number_of_integrations = int(input())

for _ in range(number_of_integrations):
    number = int(input())
    if number >= 0:
        my_positive_list.append(number)
    else:
        my_negative_list.append(number)
print(my_positive_list)
print(my_negative_list)
print(f"Count of positives: {len(my_positive_list)}")
print(f"Sum of negatives: {sum(my_negative_list)}")