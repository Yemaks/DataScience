def probability(N, M, S):
    if M > N:
        print("Не выполнено условие: M <= N")
        return

    if S > 6 or S < 1:
        print("Не выполнено условие: S ∈ [1, 6]")
        return

    factorial_N = 1
    n = N
    while n > 1:
        factorial_N *= n
        n -= 1

    factorial_M = 1
    n = M
    while n > 1:
        factorial_M *= n
        n -= 1

    factorial_N_M = 1
    n = (N - M)
    while n > 1:
        factorial_N_M *= n
        n -= 1

    chance = (factorial_N / (factorial_M * factorial_N_M)) * (((7 - S) / 6) ** M) * (((S - 1) / 6) ** (N - M))

    print("Вероятность из " + str(N) + " бросков кубика " + str(M) + " раз выбросить результат не менее "
          + str(S) + " равна: " + str(chance))


probability(19, 7, 4)
