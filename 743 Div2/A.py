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
    s = input_string()
    ret = sum(int(ch) for ch in s)
    ret += sum(int(ch != '0') for ch in s)
    if s[-1] != '0':
        ret -= 1
    print(ret)
