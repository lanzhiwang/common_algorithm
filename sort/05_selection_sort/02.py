def selection_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        collection[least], collection[i] = (
            collection[i], collection[least]
        )
    return collection


if __name__ == '__main__':
    user_input = '99 5 36 7 22 17 46 12'
    unsorted = [int(item) for item in user_input.split(' ')]
    selection_sort(unsorted)
    print(unsorted)
