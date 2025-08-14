"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

!!!! Melhorar código
"""
def myFunc(e):
    return e[1]

def getSecondUniqueLoestValue(arr):
    arr = list(dict.fromkeys(arr))
    return arr[1]


if __name__ == '__main__':
    records = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])
    
    records.sort(key=myFunc)
    """
        o parâmetro `key` do list.sort recebe uma função (não o retorno dessa função)
        e o parâmetro que a função recebe são todos os elementos da lista antes da ordenação acontecer
        e usa ele como uma regra de ordenação
    """
    
    values = list()
    for i in records:
        values.append(i[1])
    
    run_up_score = getSecondUniqueLoestValue(values)
    names = list()
    for i in records:
        if i[1] == run_up_score:
            names.append(i[0])
    
    names.sort()
    for name in names:
        print(name)