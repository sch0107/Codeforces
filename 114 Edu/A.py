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
def generate_bracket(n):
    ret = []
    def backTrack(o, c, cur):
        if len(ret) == n: return 
        if o == c == n:
            ret.append(''.join(cur))
            return
        if o < n:
            cur.append('(')
            backTrack(o+1, c, cur)
            cur.pop()
            if len(ret) == n: return 
        if c < o:
            cur.append(')')
            backTrack(o, c+1, cur)
            cur.pop()
            if len(ret) == n: return 
    backTrack(0,0,[])
    return ret
    
tests = inp()
dic = {}
shown = {}
for _ in range(tests):
    n = inp()
    if n not in dic:
        dic[n] = generate_bracket(n)
    for i in range(n):
        print(dic[n][i])
