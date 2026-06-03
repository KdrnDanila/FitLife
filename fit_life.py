WATER_PER_KG = 30
MILLILITRES_PER_LITRES = 1000
"""ввод констант для упрощения кода"""

user_name = input("Здравствуйте! Укажите ваше имя: ")
print("Приятно познакомиться,", user_name.title(), "!")
user_age = int(input("Укажите ваш возраст (полных лет): "))
user_weight = float(input("Укажите ваш вес в килограммах (например, 70.5): "))
user_height = float(input("Укажите ваш рост в метрах (например, 1.55): "))
"""переменные для сбора данных"""

bmi = user_weight / (user_height ** 2)
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / MILLILITRES_PER_LITRES
user_info = f"{user_name} {user_age}"
"""
    создаю переменые для упрощения кода:
    первая считает индекс массы тела
    вторая считает норму воды
    третья переводит норму воды в мл
    четвертая упрощает код для отчета
"""

print(f"Отчет для пользователя: {user_info} лет")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")
"""печать отчета"""
