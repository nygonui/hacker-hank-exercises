"""https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true"""

def count_substring(string, sub_string):
    aux = 0
    sub_len = len(sub_string)
    for i in range(0, len(string)):
        if sub_string == string[i:i+sub_len]:
            aux = aux + 1
    return aux
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)