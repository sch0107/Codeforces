import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_list():
    # list of integers
    return list(map(int,input().split()))
def input_string():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    # usage: m, n = input_int_gen()
    return map(int,input().split())


# Codeforce xxx Div x A
tests = inp()
for _ in range(tests):
    n = inp()
    a = input_list()
    b = input_list()
    pos = {}
    for p, num in enumerate(a):
        pos[num] = p
    for p, num in enumerate(b):
        pos[num] = p
    l, ret = n, n
    for num in range(2*n, 0, -1):
        if num%2:
            ret = min(ret, pos[num]+l)
        else:
            l = min(l, pos[num])
            
    print(ret)
