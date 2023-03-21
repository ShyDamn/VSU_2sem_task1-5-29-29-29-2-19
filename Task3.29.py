total_cost = 0 # общая стоимость товаров
discounted_cost = 0 # стоимость товаров со скидкой

price = 0
while price >= 0:
    price = float(input("Введите цену товара (для окончания введите отрицательное число): "))
    total_cost += price
    if price >= 1000:
        discounted_cost += price * 0.95
    else:
        discounted_cost += price

print(f"Общая стоимость товаров: {total_cost:.2f}")
print(f"Общая стоимость товаров со скидкой: {discounted_cost:.2f}")



