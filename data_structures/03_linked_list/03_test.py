class Link:
    next = None
    previous = None

    def __init__(self, x):
        self.value = x

    def displayLink(self):
        print("{}".format(self.value), end=" ")


if __name__ == '__main__':
    l1 = Link(1)
    l2 = Link(2)

    print(l1, l1.next, l1.previous)
    print(l2, l2.next, l2.previous)
    print(Link.next, Link.previous)

    l2.next = 2
    l2.previous = 2

    print()
    print(l1, l1.next, l1.previous)
    print(l2, l2.next, l2.previous)
    print(Link.next, Link.previous)

    Link.next = 5
    Link.previous = 5

    print()
    print(l1, l1.next, l1.previous)
    print(l2, l2.next, l2.previous)
    print(Link.next, Link.previous)

"""
<__main__.Link object at 0x7f7fb98e6f98> None None
<__main__.Link object at 0x7f7fb98e6fd0> None None
None None

<__main__.Link object at 0x7f7fb98e6f98> None None
<__main__.Link object at 0x7f7fb98e6fd0> 2 2
None None

<__main__.Link object at 0x7f7fb98e6f98> 5 5
<__main__.Link object at 0x7f7fb98e6fd0> 2 2
5 5

"""