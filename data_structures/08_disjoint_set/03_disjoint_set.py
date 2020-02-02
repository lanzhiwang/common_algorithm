#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

r"""
用树结构判断图中是否有环

graph = {
    '0': ['1'],
    '1': ['0', '2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '4'],
    '4': ['2', '3'],
    '5': ['2'],
}

[['2', '5'], ['3', '4'], ['1', '3'], ['1', '2'], ['0', '1'], ['2', '4']]
{'0': None, '1': None, '2': None, '3': None, '4': None, '5': None}
{'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0}

x_vertext: 2, y_vertext: 5
x_root:    2, y_root:    5
rank:      0, rank:      0

  5
 /
2

{'0': None, '1': None, '2': '5', '3': None, '4': None, '5': None}
{'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 1}
#############################################################################
x_vertext: 3, y_vertext: 4
x_root:    3, y_root:    4
rank:      0, rank:      0

  5
 /
2

  4
 /
3

{'0': None, '1': None, '2': '5', '3': '4', '4': None, '5': None}
{'0': 0, '1': 0, '2': 0, '3': 0, '4': 1, '5': 1}
#############################################################################
x_vertext: 1, y_vertext: 3
x_root:    1, y_root:    4
rank:      0, rank:      1

  5
 /
2

  4
 / \
3   1


{'0': None, '1': '4', '2': '5', '3': '4', '4': None, '5': None}
{'0': 0, '1': 0, '2': 0, '3': 0, '4': 1, '5': 1}
#############################################################################
x_vertext: 1, y_vertext: 2
x_root:    4, y_root:    5
rank:      1, rank:      1

  5
 / \
2   4
   / \
  3   1

{'0': None, '1': '4', '2': '5', '3': '4', '4': '5', '5': None}
{'0': 0, '1': 0, '2': 0, '3': 0, '4': 1, '5': 2}
#############################################################################
x_vertext: 0, y_vertext: 1
x_root:    0, y_root:    5
rank:      0, rank:      2

    5
 / \  \
2   4  0
   / \
  3   1


{'0': '5', '1': '4', '2': '5', '3': '4', '4': '5', '5': None}
{'0': 0, '1': 0, '2': 0, '3': 0, '4': 1, '5': 2}
#############################################################################
x_vertext: 2, y_vertext: 4
x_root:    5, y_root:    5
rank:      2, rank:      2
False
{'0': '5', '1': '4', '2': '5', '3': '4', '4': '5', '5': None}
{'0': 0, '1': 0, '2': 0, '3': 0, '4': 1, '5': 2}
#############################################################################

"""


def get_all_edge(graph):
    result = []
    for k, v in graph.items():
        for i in v:
            if sorted((k, i)) not in result:
                result.append(sorted((k, i)))
    return result


def bfs(graph, start):
    result = []
    queue = []
    seen = set()
    queue.append(start)
    seen.add(start)
    while len(queue):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        result.append(vertex)
    return result


def find_root(vertext, parent):
    root = vertext
    while parent[root] is not None:
        root = parent[root]
    return root


def union_vertices(x_vertext, y_vertext, parent, rank):
    x_root = find_root(x_vertext, parent)
    y_root = find_root(y_vertext, parent)
    print('x_vertext: %s, y_vertext: %s' % (x_vertext, y_vertext))
    print('x_root:    %s, y_root:    %s' % (x_root, y_root))
    print('rank:      %s, rank:      %s' % (rank[x_root], rank[y_root]))
    if x_root == y_root:
        return False
    else:
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        else:
            parent[x_root] = y_root
            rank[y_root] += 1
        return True


if __name__ == '__main__':
    graph = {
        '0': ['1'],
        '1': ['0', '2', '3'],
        '2': ['1', '4', '5'],
        '3': ['1', '4'],
        '4': ['2', '3'],
        '5': ['2'],
    }

    # graph = {
    #     '0': ['1'],
    #     '1': ['0', '2', '3'],
    #     '2': ['1', '5'],
    #     '3': ['1', '4'],
    #     '4': ['3'],
    #     '5': ['2'],
    # }

    all_edge = get_all_edge(graph)
    random.shuffle(all_edge)

    # all_edge = [['0', '1'], ['1', '3'], ['2', '4'], ['2', '5'], ['1', '2'], ['3', '4']]
    print(all_edge)

    vertices = bfs(graph, '0')
    # print(vertices)  # ['0', '1', '2', '3', '4', '5']

    parent = {k: None for k in vertices}
    print(parent)  # {'0': None, '1': None, '2': None, '3': None, '4': None, '5': None}

    rank = {k: 0 for k in vertices}
    print(rank)

    print()
    print()
    print()
    # for edge in all_edge:
    #     x, y = edge
    #     print(union_vertices(x, y, parent, rank))
    #     print(parent)
    #     print(rank)
    #     print('#############################################################################')

    for edge in all_edge:
        x, y = edge
        if not union_vertices(x, y, parent, rank):
            print('有环')
            break
    else:
        print('无环')
