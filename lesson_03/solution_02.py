money = 2130

for i in range(5):
    money += money * 0.1 + 120

print(money)


# alternative

money2 = 2130
money2 += money2 * 0.1 + 120
money2 += money2 * 0.1 + 120
money2 += money2 * 0.1 + 120
money2 += money2 * 0.1 + 120
money2 += money2 * 0.1 + 120

print(money2)

