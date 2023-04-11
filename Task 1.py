def unique_elements(array):
    modified_array = []
    for i in array:
        if not i in modified_array:
            modified_array.append(i)
    modified_array.sort()
    return modified_array


print(unique_elements([1, 5, 1, 7, 3, 8, 3, 2, 3, 4, 5, 5, 1, 3, 5]))
