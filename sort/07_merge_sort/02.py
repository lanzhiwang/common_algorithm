"""
collection: [10, 5, 7, 3, 2, 8, 6], start: [], end: []
collection: [5, 7, 3, 8, 6], start: [2], end: [10]
collection: [5, 7, 6], start: [2, 3], end: [10, 8]
collection: [6], start: [2, 3, 5], end: [10, 8, 7]
2,3,5,6,7,8,10

"""


def merge_sort(collection):
    if len(collection) <= 1:
        return collection

    start, end = [], []
    while len(collection) > 1:
        # print('collection: %s, start: %s, end: %s' % (collection, start, end))
        min_one, max_one = min(collection), max(collection)
        start.append(min_one)
        end.append(max_one)
        collection.remove(min_one)
        collection.remove(max_one)
    # print('collection: %s, start: %s, end: %s' % (collection, start, end))

    end.reverse()
    return start + collection + end


if __name__ == '__main__':
    unsorted = [10, 5, 7, 3, 2, 8, 6]
    print(merge_sort(unsorted))

    for unsorted in [
        [], [0], [2], [3, 5], [5, 3], [5, 5], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3], [0, 2, 2, 3, 5],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [-45, -2, -5]
    ]:
        print(unsorted)
        print(merge_sort(unsorted))
        print()
