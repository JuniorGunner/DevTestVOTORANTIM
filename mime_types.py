'''
Author: Claudemir S. F. Junior
Date: 27/05/2019
Problem: MIME Types Puzzle - codingame.com
'''

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
d = {ext: mt for ext, mt in [input().split() for _ in range(n)]} # d: dict for association table, ext: file extension, mt: MIME type.
fname = [input().lower() for _ in range(q)] # One file name per line.

for f in fname: # Percorre lista de arquivos
    if '.' in f: # Verifica se arquivo tem extensão
        x = f.split('.')[-1] # Separa extensão
        if x.lower() in d: # Verifica se extensão está na tabela
            print(d[x.lower()]) # Retorna MIME Type
        elif x.upper() in d:
            print(d[x.upper()])
        else:
            print('UNKNOWN') # Caso não esteja na tabela
    else:
        print('UNKNOWN') # Caso não tenha extensão
