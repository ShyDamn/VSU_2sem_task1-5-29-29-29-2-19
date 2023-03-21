# получаем число блюд, которые может приготовить столовая
m = int(input())
# получаем список блюд, которые может приготовить столовая
menu = set([input() for _ in range(m)])

# получаем число дней, для которых есть списки блюд
n = int(input())

# создаем множество для хранения всех блюд, которые были приготовлены
cooked_dishes = set()

# для каждого дня получаем список блюд и добавляем их в множество приготовленных блюд
for i in range(n):
    num_dishes = int(input())
    for j in range(num_dishes):
        cooked_dishes.add(input())

# выводим список блюд, которые еще ни разу не готовили
for dish in menu:
    if dish not in cooked_dishes:
        print(dish)
