# вводим константы
WATER_PER_KG = 30
MILLILITRES_PER_LITRES = 1000

# собираем данные
print("Здравствуйте! Укажите ваше имя:")
user_name = input()
print("Приятно познакомиться,", user_name.title(), "!")
print("Укажите ваш возраст:")
user_age = int(input())
print("Укажите ваш вес в килограммах (например, 70.5):")
user_weight = float(input())
print("Укажите ваш рост в метрах (например, 1.55):")
user_height = float(input())

# считаем индекс массы тела
bmi = user_weight / (user_height ** 2)

# считаем норму воды
water_ml = user_weight * WATER_PER_KG

# переводим норму воды в литры
water_l = water_ml / MILLILITRES_PER_LITRES

# создаю переменную для упрощения кода
user_info = f"{user_name.title()} {user_age}"

# печатаем отчет
print(f"Отчет для пользователя: {user_info} лет")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")
