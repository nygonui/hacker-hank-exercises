"""
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
"""
n = int(input())
s = set(map(int, input().split()))


for _ in range(int(input())):
    command, *value = input().split()

    match command:
        case 'pop':
            s.pop()
        case 'remove':
            s.remove(int(value[0]))
        case 'discard':
            s.discard(int(value[0]))

print(sum(s))

    