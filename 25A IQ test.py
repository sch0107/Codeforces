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
n = inp()
lst = input_list()
oddi = eveni = -1
oddn = evenn = 0
for i, num in enumerate(lst):
    if num % 2:
        oddi = i
        oddn += 1
    else:
        eveni = i
        evenn += 1
    if oddn and evenn:
        if oddn>evenn:
            print(eveni+1)
            break
        elif evenn>oddn:
            print(oddi+1)
            break