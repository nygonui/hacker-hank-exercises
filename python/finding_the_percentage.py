"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
"""

if __name__ == '__main__':
    n = int(input())
    students_marks = {}
    for _ in range(n):
        name, *line = input().split()
        """
            - input().split(): vai retornar uma lista, resultado do split da string de entrada
            - split(): por padrão ele splita por espaços em branco
            - name, *line: o primeiro valor do split vai para `name` o restante 
            vira uma lista e vai para `line`
            - *line: nesse caso ele está fazendo UNPACKING ITERABLES
        """
        scores = list(map(float, line))
        """
            - map(func, iterable): aplica uma função para todos os itens de um iterável (lista, dict ...)
        """
        students_marks[name] = scores
        """
            - students_mark: é um dict (relação de chave e valor)
            - students_marks[name] = scores: definindo os valores (scores) para chave (name)
        """
    query_name = input()
    result = sum(students_marks[query_name])/len(students_marks[query_name])
    print(f'{result:.2f}')
