import math


def cosine_distance(vector_a, vector_b):
    a_times_b = 0
    norm_a = 0
    norm_b = 0
    for i in range(0, len(vector_a)):
        a_times_b += vector_a[i] * vector_b[i]
        norm_a += vector_a[i] * vector_a[i]
        norm_b += vector_b[i] * vector_b[i]
    norm_a = norm_a ** (0.5)
    norm_b = norm_b ** (0.5)
    if (norm_a == 0) or (norm_b == 0):
        return print("Вычислить косинусное расстояние невозможно: как минимум один из векторов нулевой")
    cosine = a_times_b / (norm_a * norm_b)
    if cosine == 0:
        return print("Вычислить косинусное расстояние невозможно: векторы перпендикулярны")
    cos_distance = 1 / (math.cos(cosine) * math.pi)
    return print("Косинусное расстояние: " + str(cos_distance))


cosine_distance([0, 2, 1], [0, 1, 0])
