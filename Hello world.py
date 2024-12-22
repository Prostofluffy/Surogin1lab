def what_to_wear(temperature, precipitation, heavy_precipitation):
    if 20 < temperature < 30:
        if precipitation:
            return "Футболку, шорты и зонт"
        else:
            return "Футболку и шорты"
    else:
        if temperature < 0:
            return "Пуховик"
        elif precipitation:
            if heavy_precipitation:
                return "Пальто, непромокаемые сапоги и зонт"
            else:
                return "Пальто и дождевик"
        else:
            return "Пальто и дождевик"


try:
    temperature: int = int(input("Введите температуру (в градусах): "))
except ValueError:
    print("Ошибка: введите числовое значение температуры.")
    exit()

precipitation_input = input("Есть ли осадки? (да/нет): ").strip().lower()

if precipitation_input == "да":
    precipitation = True
    heavy_precipitation_input = input("Осадки сильные? (да/нет): ").strip().lower()
    heavy_precipitation = heavy_precipitation_input == "да"
elif precipitation_input == "нет":
    precipitation = False
    heavy_precipitation = False
else:
    print("Ошибка: введите 'да' или 'нет' для осадков.")
    exit()
result = what_to_wear(temperature, precipitation, heavy_precipitation)
print(f"Рекомендуемая одежда: {result}")
