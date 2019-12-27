# -*- coding: utf-8 -*-
"""

"""


class my_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def getdata(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getheight(self):
        return self.height

    def setdata(self, data):
        self.data = data
        return

    def setleft(self, node):
        self.left = node
        return

    def setright(self, node):
        self.right = node
        return

    def setheight(self, height):
        self.height = height
        return
