#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""


class Article(object):
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price

    def __str__(self):
        return 'weight: %s, price: %s' % (self.weight, self.price)


if __name__ == '__main__':
    max_weight = 8
    articles = []
    for i in [(0, 0), (2, 3), (3, 4), (4, 5), (5, 6)]:
        articles.append(Article(*i))

    matrix = {
        0: [0] * (max_weight + 1),
        1: [0] * (max_weight + 1),
        2: [0] * (max_weight + 1),
        3: [0] * (max_weight + 1),
        4: [0] * (max_weight + 1)
    }

    for i in range(1, 5):
        for j in range(1, 9):
            weight = articles[i].weight
            price = articles[i].price
            if weight > j:
                matrix[i][j] = matrix[i - 1][j]
            else:  # weight <= j
                no_select = matrix[i - 1][j]
                select = price + matrix[i - 1][j - weight]
                matrix[i][j] = max(no_select, select)

    print(matrix)
    """
    {
    0: [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    1: [0, 0, 3, 3, 3, 3, 3, 3, 3], 
    2: [0, 0, 3, 4, 4, 7, 7, 7, 7], 
    3: [0, 0, 3, 4, 5, 7, 8, 9, 9], 
    4: [0, 0, 3, 4, 5, 7, 8, 9, 10]
    }
    """

    # 回溯
    result = []
    max_price = matrix[4][8]
    print(max_price)
    i = 4
    j = 8
    while i > 0 and j > 0:
        if matrix[i][j] == matrix[i-1][j]:
            # no_select
            i -= 1

        else:
            # select
            result.append(i)
            j = j - articles[i].weight
            i = i - 1
    print(result)
