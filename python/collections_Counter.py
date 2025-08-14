from collections import Counter
X = int(input())
shoes_list = list(map(int, input().split()))
size_count = Counter(shoes_list)

soma = 0

for _ in range(int(input())):
    size, price = list(map(int, input().split()))
    if size in size_count:
        if size_count[size] > 0:
            size_count[size] -= 1
            soma += price
            
print(soma)
