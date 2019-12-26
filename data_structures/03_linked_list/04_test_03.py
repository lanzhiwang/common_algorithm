# -*- coding: utf-8 -*-

"""
链表的翻转
https://zhuanlan.zhihu.com/p/38521018

head
1 -> 2 -> 3 -> 4 -> 5

1 -> 2 -> 3 -> 4 -> 5
p    q    r

p.next = None
q.next = p
p = q
q = r
r = r.next


1 <- 2  3 -> 4 -> 5
     p  q    r

q.next = p
p = q
q = r
r = r.next

1 <- 2 <- 3  4 -> 5
          p  q    r

q.next = p
p = q
q = r
r = r.next

1 <- 2 <- 3 <- 4  5
               p  q r


q.next = p
p = q
q = r
r = r.next

1 <- 2 <- 3 <- 4 <- 5
                    p q=None

head = p

"""
