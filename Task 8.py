import random


def distribution_random_numbers(array_random_nimbers):
    array_random_nimbers.sort()

    if len(array_random_nimbers) % 2 == 0:
        median = (array_random_nimbers[int(len(array_random_nimbers) / 2)] +
                  array_random_nimbers[int(len(array_random_nimbers) / 2) - 1]) / 2
    else:
        median = array_random_nimbers[int((len(array_random_nimbers) - 1) / 2)]

    modes = [[], []]
    for i in range(len(array_random_nimbers)):
        if array_random_nimbers[i] in modes[0]:
            modes[1][modes[0].index(array_random_nimbers[i])] += 1
        else:
            modes[0].append(array_random_nimbers[i])
            modes[1].append(1)

    if modes[1].count(max(modes[1])) == 1:
        mode = modes[0][modes[1].index(max(modes[1]))]
    else:
        mode = []
        for i in range(len(modes[0])):
            if modes[1][i] == max(modes[1]):
                mode.append(modes[0][i])

    sum_elem = 0
    for i in range(len(array_random_nimbers)):
        sum_elem += array_random_nimbers[i]

    average = sum_elem / len(array_random_nimbers)

    print("Среднее арифметическое = " + str(average))
    if modes[1].count(max(modes[1])) == 1:
        print("Мода = " + str(mode) + "; частота " + str(max(modes[1])))
        average_mode = mode
    else:
        print("Моды = " + str(mode) + "; частота " + str(max(modes[1])))
        sum_mode = 0
        for i in range(len(mode)):
            sum_mode += mode[i]
        average_mode = sum_mode / len(mode)
        print("Среднее из мод = " + str(average_mode))
    print("Медиана = " + str(median))

    if int(average) == int(average_mode) == int(median):
        print("Распределение случайных чисел симметрично")
    else:
        print("Распределение случайных чисел асимметрично")


array_random_nimbers = []
length = 10_000
for i in range(length):
    array_random_nimbers.append(random.randint(1, 1000))

distribution_random_numbers(array_random_nimbers)
