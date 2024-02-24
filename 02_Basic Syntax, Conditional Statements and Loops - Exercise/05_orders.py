number_of_orders = int(input())
total_amount = 0
order_price = 0.0

for number_of_orders in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())
    if not 0.01 <= price_per_capsule <= 100:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= capsule_needed_per_day <= 2000:
        continue

    order_price = capsule_needed_per_day * days * price_per_capsule
    print(f"The price for the coffee is: ${order_price:.2f}")
    total_amount += order_price
print(f'Total: ${total_amount:.2f}')
