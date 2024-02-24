lost_battles = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_broken_helmets = lost_battles // 2
total_broken_sword = lost_battles // 3
total_broken_shield = lost_battles // (2 * 3)
total_broken_armor = total_broken_shield // 2
expenses = total_broken_helmets * helmet_price \
           + total_broken_sword * sword_price \
           + total_broken_shield * shield_price \
           + total_broken_armor * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
