"""
Output:

Enter a Postfix Equation (space separated) = 5 6 9 * +
 Symbol  |    Action    | Stack
-----------------------------------
       5 | push(5)      | 5
       6 | push(6)      | 5,6
       9 | push(9)      | 5,6,9
         | pop(9)       | 5,6
         | pop(6)       | 5
       * | push(6*9)    | 5,54
         | pop(54)      | 5
         | pop(5)       |
       + | push(5+54)   | 59

	Result =  59
"""

import operator as op


def Solve(Postfix):
    print('Postfix: %s' % Postfix)  # Postfix: ['5', '6', '9', '*', '+']
    Stack = []
    Div = lambda x, y: int(x/y)
    Opr = {'^': op.pow, '*': op.mul, '/': Div, '+': op.add, '-': op.sub}

    for x in Postfix:
        print('x: %s' % x)
        print(Stack)
        if x.isdigit():
            Stack.append(x)
        else:
            B = Stack.pop()
            A = Stack.pop()

            Stack.append(str(Opr[x](int(A), int(B))))
        print(Stack)

    return int(Stack[0])


if __name__ == "__main__":
    Postfix = '5 6 9 * +'.split(' ')
    print("\n\tResult = ", Solve(Postfix))
