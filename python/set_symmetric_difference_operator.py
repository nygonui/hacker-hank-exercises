"""
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
"""

e = int(input())
n_e = set(map(int, input().split()))
f = int(input())
n_f = set(map(int, input().split()))

print(len(n_e.symmetric_difference(n_f)))