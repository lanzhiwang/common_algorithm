#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://www.youtube.com/watch?v=9wV1VxlfBlI

从 BFS 到 Dijkstra 算法

Dijkstra 算法是 BFS 的升级版。当一个图中的每条边都加上权值后，BFS 就没办法求一个点到另一个点的最短路径了。
这时候，需要用到 Dijkstra 算法。从最基本原理上讲，把 BFS 改成 Dijkstra 算法，只需要把“队列”改成“优先队列”就可以了。

"""