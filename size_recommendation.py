def recommend_size(height, weight):
    if weight > 80:
        return "L"
    elif weight < 60:
        return "S"
    else:
        return "M"

# Тест
height = float(input("Введите рост (см): "))
weight = float(input("Введите вес (кг): "))
size = recommend_size(height, weight)
print(f"Рекомендуемый размер: {size}")