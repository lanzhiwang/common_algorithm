def shell_sort(collection):
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap  # 4
        while i < len(collection):  # 4
            print(collection)
            temp = collection[i]  # 2
            j = i  # 4
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1
            print(collection)

    return collection


if __name__ == '__main__':
    unsorted = [8, 9, 1, 7, 2, 3, 5, 4, 6, 0]
    print(shell_sort(unsorted))

