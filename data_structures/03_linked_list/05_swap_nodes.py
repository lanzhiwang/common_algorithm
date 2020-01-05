class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        if self.next is not None:
            return 'data: %s, next: %s' % (self.data, self.next.data)
        else:
            return 'data: %s, next: %s' % (self.data, None)



class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    """adding nodes
    push(5)
    push(4)
    push(3)
    push(2)
    push(1)
    
    (1, ->) (2, ->) (3, ->) (4, ->) (5, None)
    head
    
    """
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    """swapping nodes
    swapNodes(1, 4)
    
    (1, ->) (2, ->) (3, ->) (4, ->) (5, None)
    head
    
    假设 D1 和 D2 不相等
    D1       | prevD1
    -------- | ------
    None     | None
    head     | None
    not head | head
    not head | not head
    
    D2       | prevD2
    -------- | ------
    None     | None
    head     | None
    not head | head
    not head | not head
    
    D1       | prevD1   | D2       | prevD2
    -------- | ------   | -------- | ------
    None     | None     | xxx      | xxx      -> 直接返回，不用交换
    
    head     | None     | None     | None     -> 直接返回，不用交换
    head     | None     | not head | head     -> 正常交换
    head     | None     | not head | not head -> 正常交换
    
    not head | head     | None     | None     -> 直接返回，不用交换
    not head | head     | head     | None     -> 正常交换
    not head | head     | not head | not head -> 正常交换
    
    not head | not head | None     | None     -> 直接返回，不用交换
    not head | not head | head     | None     -> 正常交换
    not head | not head | not head | head     -> 正常交换
    not head | not head | not head | not head -> 正常交换

    """
    def swapNodes(self, d1, d2):
        prevD1 = None
        prevD2 = None
        if d1 == d2:
            return
        else:
            # find d1
            D1 = self.head
            while D1 is not None and D1.data != d1:
                prevD1 = D1
                D1 = D1.next
            # find d2
            D2 = self.head
            while D2 is not None and D2.data != d2:
                prevD2 = D2
                D2 = D2.next

            if D1 is None and D2 is None:
                return




            # if D1 is head
            if prevD1 is not None:
                prevD1.next = D2
            else:
                self.head = D2


            # if D2 is head
            if prevD2 is not None:
                prevD2.next = D1
            else:
                self.head = D1
            temp = D1.next
            D1.next = D2.next
            D2.next = temp

# swapping code ends here



if __name__ == '__main__':
    list = Linkedlist()
    list.push(5)
    list.push(4)
    list.push(3)
    list.push(2)
    list.push(1)

    list.print_list()  # 1 2 3 4 5

    list.swapNodes(1, 4)
    print("After swapping")
    list.print_list()
    # 4 2 3 1 5
