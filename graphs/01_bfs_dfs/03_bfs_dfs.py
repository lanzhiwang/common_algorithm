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
    '0': ['1'],
    '1': ['0', '2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '4'],
    '4': ['2', '3'],
    '5': ['2'],
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


print(bfs(graph, '0'))  # ['0', '1', '2', '3', '4', '5']
print(bfs(graph, '2'))  # ['2', '1', '4', '5', '0', '3']


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


print(dfs(graph, '0'))  # ['0', '1', '3', '4', '2', '5']
print(dfs(graph, '2'))  # ['2', '5', '4', '3', '1', '0']
