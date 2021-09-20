import sys
from bisect import bisect_left
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
heron = inp()
herolst = input_list()
herolst.sort()
herot = sum(herolst)
tests = inp()
for _ in range(tests):
    dragon = input_list()
    defense, attack = dragon[0], dragon[1]
    # if attack>=herot:
    #     # print('A')
    #     print(defense+attack-herot)
    if defense >= herolst[-1]:
        # print('B')
        d = defense - herolst[-1]
        d += max(0, attack - herot + herolst[-1])
        print(d)
    else:
        # l, r = 0, heron
        # while l<r:
        #     mid = (l+r+1)//2
        #     if herolst[mid]>defense:
        #         r = mid - 1
        #     else:
        #         l = mid
        # print('C')
        l = bisect_left(herolst, defense)
        print(max(0, min(
            max(0, (defense - herolst[l-1])) + max(0, attack - herot + herolst[l-1]),
            attack - herot +  herolst[l]
        )))