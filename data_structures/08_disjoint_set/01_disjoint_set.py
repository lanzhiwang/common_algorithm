#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

"""
检查图数据和结构或者链表数据结构中是否存在环
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


if __name__ == '__main__':
    graph = {
        '0': ['1'],
        '1': ['0', '2', '3'],
        '2': ['1', '4', '5'],
        '3': ['1', '4'],
        '4': ['2', '3'],
        '5': ['2'],
    }
    all_edge = get_all_edge(graph)
    random.shuffle(all_edge)
    print(all_edge)
    print(bfs(graph, '0'))  # ['0', '1', '2', '3', '4', '5']
    """
    ['0', '1', '2', '3', '4', '5']
    [['1', '3'], ['3', '4'], ['2', '5'], ['1', '2'], ['0', '1'], ['2', '4']]
    
    ['1', '3']
    disjoint set
    1, 3
    
    ['3', '4'] -> 一个点在集合中，另一个不在集合中
    disjoint set
    1, 3, 4
    
    ['2', '5'] -> 两个点都不在同一集合中
    disjoint set 1
    1, 3, 4
    disjoint set 2
    2, 5
    
    ['1', '2'] -> 两个点分别在不同的集合中，合并集合
    disjoint set
    1, 3, 4, 2, 5
    
    ['0', '1'] -> 一个点在集合中，另一个不在集合中
    disjoint set
    1, 3, 4, 2, 5, 0
    
    ['2', '4'] -> 两个点都在同一个集合中，说明有环
    
    """

    graph = {
        '0': ['1'],
        '1': ['0', '2', '3'],
        '2': ['1', '5'],
        '3': ['1', '4'],
        '4': ['3'],
        '5': ['2'],
    }
    all_edge = get_all_edge(graph)
    random.shuffle(all_edge)
    print(all_edge)
    print(bfs(graph, '0'))  # ['0', '1', '2', '3', '4', '5']
    """
    [['3', '4'], ['1', '3'], ['0', '1'], ['1', '2'], ['2', '5']]
    ['0', '1', '2', '3', '5', '4']
    
    ['3', '4']
    disjoint set
    3, 4
    
    ['1', '3']
    disjoint set
    3, 4, 1
    
    ['0', '1']
    disjoint set
    3, 4, 1, 0
    
    ['1', '2']
    disjoint set
    3, 4, 1, 0, 2
    
    ['2', '5']
    disjoint set
    3, 4, 1, 0, 2, 5
    
    图中无环
    
    """

    graph = {
        '0': ['1'],
        '1': ['0', '2'],
        '2': ['1', '3'],
        '3': ['2']
    }
    all_edge = get_all_edge(graph)
    random.shuffle(all_edge)
    print(all_edge)
    print(bfs(graph, '0'))
    """
    [['2', '3'], ['0', '1'], ['1', '2']]
    ['0', '1', '2', '3']
    
    ['2', '3']
    disjoint set
    2, 3
    
    ['0', '1']
    disjoint set1
    2, 3
    disjoint set2
    0, 1
    
    ['1', '2']
    disjoint set
    0, 1, 2, 3
    
    链表中无环

    """

    graph = {
        '0': ['1'],
        '1': ['0', '2'],
        '2': ['1', '3'],
        '3': ['2', '4', '6'],
        '4': ['3', '5'],
        '5': ['4', '6'],
        '6': ['3', '5']
    }
    all_edge = get_all_edge(graph)
    random.shuffle(all_edge)
    print(all_edge)
    print(bfs(graph, '0'))
    """
    [['2', '3'], ['5', '6'], ['3', '4'], ['0', '1'], ['1', '2'], ['3', '6'], ['4', '5']]
    ['0', '1', '2', '3', '4', '6', '5']
    
    ['2', '3']
    disjoint set
    2, 3
    
    ['5', '6']
    disjoint set1
    2, 3
    disjoint set2
    5, 6
    
    ['3', '4']
    disjoint set1
    2, 3, 4
    disjoint set2
    5, 6
    
    ['0', '1']
    disjoint set1
    2, 3, 4
    disjoint set2
    5, 6
    disjoint set3
    0, 1
    
    ['1', '2']
    disjoint set1
    2, 3, 4, 1, 0
    disjoint set2
    5, 6
    
    ['3', '6']
    disjoint set
    2, 3, 4, 1, 0, 5, 6
    
    ['4', '5'] 链表中有环

    """
