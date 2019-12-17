"""
collection: [10, 5, 7, 3, 2, 8, 6], start: [], end: []
collection: [5, 7, 3, 8, 6], start: [2], end: [10]
collection: [5, 7, 6], start: [2, 3], end: [10, 8]
collection: [6], start: [2, 3, 5], end: [10, 8, 7]
2,3,5,6,7,8,10

"""


def merge_sort(collection):
    start, end = [], []
    while len(collection) > 1:
        print('collection: %s, start: %s, end: %s' % (collection, start, end))
        min_one, max_one = min(collection), max(collection)
        start.append(min_one)
        end.append(max_one)
        collection.remove(min_one)
        collection.remove(max_one)
    print('collection: %s, start: %s, end: %s' % (collection, start, end))

    end.reverse()
    return start + collection + end


if __name__ == '__main__':
    user_input = '10, 5, 7, 3, 2, 8, 6'
    unsorted = [int(item) for item in user_input.split(',')]
    print(*merge_sort(unsorted), sep=',')






