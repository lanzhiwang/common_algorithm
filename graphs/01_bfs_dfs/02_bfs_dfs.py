#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
import math

"""
https://www.youtube.com/watch?v=9wV1VxlfBlI

从 BFS 到 Dijkstra 算法

Dijkstra 算法是 BFS 的升级版。当一个图中的每条边都加上权值后，BFS 就没办法求一个点到另一个点的最短路径了。
这时候，需要用到 Dijkstra 算法。从最基本原理上讲，把 BFS 改成 Dijkstra 算法，只需要把“队列”改成“优先队列”就可以了。

基础: python 优先队列的使用方法
>>> import heapq
>>> pqueue = []
>>> heapq.heappush(pqueue, (1, 'A'))
>>> heapq.heappush(pqueue, (7, 'B'))
>>> heapq.heappush(pqueue, (3, 'C'))
>>> heapq.heappush(pqueue, (6, 'D'))
>>> heapq.heappush(pqueue, (2, 'E'))
>>> heapq.heappush(pqueue, (3, 'F'))
>>>
>>> heapq.heappop(pqueue)
(1, 'A')
>>> heapq.heappop(pqueue)
(2, 'E')
>>> heapq.heappop(pqueue)
(3, 'C')
>>> heapq.heappop(pqueue)
(3, 'F')
>>> heapq.heappop(pqueue)
(6, 'D')
>>> heapq.heappop(pqueue)
(7, 'B')
>>> heapq.heappop(pqueue)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index out of range

基础: python 集合使用方法
>>> seen = set()
>>> seen.add('A')
>>> seen.add('B')
>>> seen.add('C')
>>> seen.add('A')
>>> seen
{'B', 'C', 'A'}
>>>


graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6},
}
start = A

########################################
初始化:
          A    B    C    D    E    F
parent:   None None None None None None
distance: 0    inf  inf  inf  inf  inf
result:   
priority queue:
(0, A)
########################################
(0, A)
priority queue:{'B': 5, 'C': 1}
(5, B)(1, C)
(1, C)(5, B)

          A    B    C    D    E    F
parent:   None A    A    None None None
distance: 0    5    1    inf  inf  inf
result: A
priority queue:
(1, C)(5, B)

########################################
(1, C)
priority queue:{'A': 1, 'B': 2, 'D': 4, 'E': 8}
(5, B)(3, B)(5, D)(9,E)
(3, B)(5, B)(5, D)(9,E)

          A    B    C    D    E    F
parent:   None C    A    C    C    None
distance: 0    3    1    5    9    inf
result: A C
priority queue:
(3, B)(5, B)(5, D)(9,E)
########################################
(3, B)
priority queue:{'A': 5, 'C': 2, 'D': 1},
(5, B)(5, D)(9,E)(4, D)
(4, D)(5, B)(5, D)(9,E)

          A    B    C    D    E    F
parent:   None C    A    B    C    None
distance: 0    3    1    4    9    inf
result: A C B
priority queue:
(4, D)(5, B)(5, D)(9,E)
########################################
(4, D)
priority queue:{'B': 1, 'C': 4, 'E': 3, 'F': 6},
(5, B)(5, D)(9,E)(7, E)(10, F)
(5, B)(5, D)(7, E)(9,E)(10, F)


          A    B    C    D    E    F
parent:   None C    A    B    D    D
distance: 0    3    1    4    7    10
result: A C B D
priority queue:
(5, B)(5, D)(7, E)(9,E)(10, F)
########################################
(5, B)
priority queue:
(5, D)(7, E)(9,E)(10, F)

          A    B    C    D    E    F
parent:   None C    A    B    D    D
distance: 0    3    1    4    7    10
result: A C B D
priority queue:
(5, D)(7, E)(9,E)(10, F)
########################################
(5, D)
priority queue:
(7, E)(9,E)(10, F)

          A    B    C    D    E    F
parent:   None C    A    B    D    D
distance: 0    3    1    4    7    10
result: A C B D
priority queue:
(7, E)(9,E)(10, F)
########################################
(7, E)
priority queue:{'C': 8, 'D': 3}
(9,E)(10, F)

          A    B    C    D    E    F
parent:   None C    A    B    D    D
distance: 0    3    1    4    7    10
result: A C B D E
priority queue:
(9,E)(10, F)
########################################
(9,E)
priority queue:
(10, F)

          A    B    C    D    E    F
parent:   None C    A    B    D    D
distance: 0    3    1    4    7    10
result: A C B D E
priority queue:
(10, F)
########################################
(10, F)
priority queue:{'D': 6}

          A    B    C    D    E    F
parent:   None C    A    B    D    D
distance: 0    3    1    4    7    10
result: A C B D E F
priority queue:
########################################
"""

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6},
}


def dijkstra(graph, start):
    parent = {key: None for key in graph.keys()}
    # print(parent)  # {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}

    distance = {}
    for key in graph.keys():
        if key == start:
            distance[key] = 0
        else:
            distance[key] = math.inf
    # print(distance)  # {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}

    result = []

    pqueue = []
    heapq.heappush(pqueue, (0, start))

    while len(pqueue):
        dist, vertex = heapq.heappop(pqueue)
        for w in graph[vertex].keys():
            if w not in result:
                heapq.heappush(pqueue, (graph[vertex][w] + dist, w))
                if graph[vertex][w] + dist < distance[w]:
                    distance[w] = graph[vertex][w] + dist
                    parent[w] = vertex
        if vertex not in result:
            result.append(vertex)
    return result, parent, distance


result, parent, distance = dijkstra(graph, 'A')
print(result)
print(parent)
print(distance)

print()

result, parent, distance = dijkstra(graph, 'B')
print(result)
print(parent)
print(distance)