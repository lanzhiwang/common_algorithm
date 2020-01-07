"""
Output:

Enter an Infix Equation = a + b ^c
 Symbol  |  Stack  | Postfix
----------------------------
   c     |         | c
   ^     | ^       | c
   b     | ^       | cb
   +     | +       | cb^
   a     | +       | cb^a
         |         | cb^a+

	 a+b^c (Infix) ->  +a^bc (Prefix)
"""


def infix_2_postfix(Infix):  # c^b+a
    Stack = []
    Postfix = []
    priority = {'^': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1}

    for x in Infix:
        if x.isalpha() or x.isdigit():
            Postfix.append(x)
        elif x == '(':
            Stack.append(x)
        elif x == ')':
            while Stack[-1] != '(':
                Postfix.append(Stack.pop())
            Stack.pop()
        else:
            if len(Stack)==0:
                Stack.append(x)
            else:
                while len(Stack) > 0 and priority[x] <= priority[Stack[-1]]:
                    Postfix.append(Stack.pop())
                Stack.append(x)

    while len(Stack) > 0:
        Postfix.append(Stack.pop())

    return "".join(Postfix)


def infix_2_prefix(Infix):
    Infix = list(Infix[::-1])
    # print(Infix)  # ['c', '^', 'b', '+', 'a']

    for i in range(len(Infix)):
        if Infix[i] == '(':
            Infix[i] = ')'
        elif Infix[i] == ')':
            Infix[i] = '('
    # print(Infix)  # ['c', '^', 'b', '+', 'a']

    Infix = "".join(Infix)
    # print(Infix)  # c^b+a

    l = infix_2_postfix(Infix)
    # print('l: %s' % l)  # cb^a+

    return l[::-1]


if __name__ == "__main__":
    Infix = 'a+b^c'
    print("\n\t", Infix, "(Infix) -> ", infix_2_prefix(Infix), "(Prefix)")
