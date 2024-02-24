number_of_cities = int(input())
total_profit = 0
for current_city in range(1, number_of_cities + 1):
    city = input()
    earned_money = float(input())
    expenses = float(input())
    if current_city % 5 == 0:
        earned_money = earned_money * 0.90
    elif current_city % 3 == 0:
        expenses = expenses * 1.50
    profit = earned_money - expenses
    total_profit += profit
    print(f"In {city} Burger Bus earned {profit:.2f} leva.")


print(f"Burger Bus total profit: {total_profit:.2f} leva.")
