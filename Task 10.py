def local_minimum(left_border, right_border):
    # Т.к. первая производная функции f(x) = 3*x^3 + 4*x^2 +5*x + 21, f`(x) = 9*x^2 + 8*x + 5 не имеет вещественных
    # корней, поэтому данная f(x) монотонно возрастает, следовательно локальный минимум на интервале будет равен
    # значению данной функции на левой границе интервала
    f_left_border = 3 * (left_border ** 3) + 4 * (left_border ** 2) + 5 * left_border + 21
    return f_left_border


print(local_minimum(2, 20))
