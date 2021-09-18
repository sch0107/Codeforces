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
    ret = n
    dica = {}
    monostk = []
    for i, num in enumerate(a):
        
        dica[num] = i
    for i, num in enumerate(b):
        ret = min(ret, i+dica[num-1])
    print(ret)
