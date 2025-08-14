"""
https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
"""

e = int(input())
n_e = set(map(int, input().split()))

f = int(input())
n_f = set(map(int, input().split()))

print(len(n_e.intersection(n_f)))