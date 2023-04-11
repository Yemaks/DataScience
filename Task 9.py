def search_query(search_queries):
    queries_length = []
    for i in search_queries:
        queries_length.append(len(i.split()))

    queries_length.sort()
    temp = queries_length[0]
    quantities = [[], []]
    j = -1
    for i in range(len(queries_length)):
        if queries_length[i] == temp and i != 0:
            quantities[1][j] += 1
        else:
            quantities[0].append(queries_length[i])
            quantities[1].append(1)
            j += 1
        temp = queries_length[i]
    for i in range(len(quantities[0])):
        quantities[1][i] = quantities[1][i] / len(search_queries) * 100
    return quantities


search_queries = ["watch new movies",
                  "coffee near me",
                  "how to find the determinant",
                  "python",
                  "data science jobs in UK",
                  "courses for data science",
                  "taxi",
                  "google",
                  "yandex",
                  "bing",
                  "foreign exchange rates USD/BYN",
                  "Netflix movies watch online free",
                  "Statistics courses online from top universities"]

print("Количество слов в запросах " + str(search_query(search_queries)[0]))
print("Процент от общего числа запросов " + str(search_query(search_queries)[1]))
