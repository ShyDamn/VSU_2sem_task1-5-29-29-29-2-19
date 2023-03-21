N = int(input("Введите количество школьников: "))
K = int(input("Введите количество яблок: "))

apples_per_student = K // N
apples_in_basket = K % N

print(f"Каждому школьнику достанется {apples_per_student} яблок")
print(f"В корзине останется {apples_in_basket} яблок")
