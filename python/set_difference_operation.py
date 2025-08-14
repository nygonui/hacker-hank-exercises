"""
https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
"""

e = int(input())
n_e = set(map(int, input().split()))
f = int(input())
n_f = set(map(int, input().split()))

print(len(n_e.difference(n_f)))