"""

"""


def calculateSpan(price, S):
    print('price: %s' % price)  # price: [10, 4, 5, 90, 120, 80]
    print('S: %s' % S)  # S: [0, 0, 0, 0, 0, 0, 0]

    n = len(price)  # 6

    st = []
    st.append(0)

    S[0] = 1

    for i in range(1, n):  # 1 2 3 4 5
        print('i: %s' % i)
        print('st: %s' % st)
        print('S: %s' % S)
        while len(st) > 0 and price[st[0]] <= price[i]:
            st.pop()
        print('st: %s' % st)

        if len(st) <= 0:
            S[i] = i + 1
        else:
            S[i] = i - st[0]
        print('S: %s' % S)

        st.append(i)
        print('st: %s' % st)
        print()

"""
i: 1
st: [0]
S: [1, 0, 0, 0, 0, 0, 0]
st: [0]
S: [1, 1, 0, 0, 0, 0, 0]
st: [0, 1]

i: 2
st: [0, 1]
S: [1, 1, 0, 0, 0, 0, 0]
st: [0, 1]
S: [1, 1, 2, 0, 0, 0, 0]
st: [0, 1, 2]

i: 3
st: [0, 1, 2]
S: [1, 1, 2, 0, 0, 0, 0]
st: []
S: [1, 1, 2, 4, 0, 0, 0]
st: [3]

i: 4
st: [3]
S: [1, 1, 2, 4, 0, 0, 0]
st: []
S: [1, 1, 2, 4, 5, 0, 0]
st: [4]

i: 5
st: [4]
S: [1, 1, 2, 4, 5, 0, 0]
st: [4]
S: [1, 1, 2, 4, 5, 1, 0]
st: [4, 5]

"""


# A utility function to print elements of array
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")


price = [10, 4, 5, 90, 120, 80]
S = [0] * (len(price) + 1)
# print(S)  # [0, 0, 0, 0, 0, 0, 0]

# Fill the span values in array S[]
calculateSpan(price, S)

# Print the calculated span values
printArray(S, len(price))
