'''
Author: Claudemir S. F. Junior
Date: 27/05/2019
Problem: MIME Types Puzzle - codingame.com
'''

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
d = {ext: mt for ext, mt in [input().split() for _ in range(n)]} # d: dict for association table, ext: file extension, mt: MIME type.
fname = [input().lower() for _ in range(q)] # One file name per line.

for f in fname: # Go through files list
    if '.' in f: # Checks if file has extension
        x = f.split('.')[-1] # Split extension
        if x in d: # Checks if extension is in table
            print(d[x]) # Returns MIME Type
        elif x.upper() in d:
            print(d[x.upper()])
        else:
            print('UNKNOWN') # If extension isn't in table
    else:
        print('UNKNOWN') # If file doesn't have extension
