grade = ""
def grades(some_number:float) ->float:
    if 2.00 <= some_number <= 2.99:
        grade = "Fail"
    elif 3.00 <= some_number <= 3.49:
        grade = "Poor"
    elif 3.50 <= some_number <= 4.49:
        grade = "Good"
    elif 4.50 <= some_number <= 5.49:
        grade = "Very Good"
    elif 5.50 <= some_number <= 6.00:
        grade = "Excellent"
    return grade


number = float(input())
result = grades(number)
print(result)
