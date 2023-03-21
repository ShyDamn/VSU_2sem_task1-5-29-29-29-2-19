print('Введите значения по порядку через запятую, первую часть строки от другой разделите точкой с запятой: ')
input_str = input()  # считываем входную строку
journals = input_str.split(";")  # разбиваем на список журналов
result = []  # список для хранения найденных сумм

for journal in journals:
    amounts = journal.split(",")  # разбиваем журнал на список сумм
    big_amounts = [int(amount) for amount in amounts if int(amount) >= 1000000000]  # выбираем только большие суммы
    if big_amounts:
        result.append(big_amounts)  # добавляем найденные суммы в результат

# выводим результат в нужном формате
for journal in result:
    print(",".join(str(amount) for amount in journal))

