#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://www.youtube.com/watch?v=oLtvUWpAnTQ
https://www.youtube.com/watch?v=bD8RT0ub--0

BFS 广度优先搜索
    使用 队列 数据结构

DFS 深度优先搜索
    使用 栈 数据结构

"""

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D'],
}


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


print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
print(bfs(graph, 'E'))  # ['E', 'C', 'D', 'A', 'B', 'F']


def dfs(graph, start):
    result = []
    stack = []
    seen = set()
    stack.append(start)
    seen.add(start)
    while len(stack):
        vertex = stack.pop(-1)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        result.append(vertex)
    return result


print(dfs(graph, 'A'))  # ['A', 'C', 'E', 'D', 'F', 'B']
print(dfs(graph, 'E'))  # ['E', 'D', 'F', 'B', 'A', 'C']


"""
最短路径

        ['A',  'B', 'C', 'D', 'E', 'F']
parent: [None, 'A', 'A', 'B', 'C', 'D']

E <- C <- A<- None

"""


def shortest_path(graph, start):
    parent = {}
    queue = []
    seen = set()
    queue.append(start)
    seen.add(start)
    parent[start] = None
    while len(queue):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = vertex
    return parent


print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
parent = shortest_path(graph, 'A')
print(parent)  # {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'C', 'F': 'D'}
for p in bfs(graph, 'A'):
    print(p, parent[p])

start = 'E'
end = 'A'

v = start
while v is not None:
    print(v)
    v = parent[v]

