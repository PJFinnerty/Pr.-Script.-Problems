#Peter Finnerty

#Method 1 for opening files:
f = open('.gitignore', 'r')

for line in f:
    print(line, end='')

f.close()

#Method 2:
with open('.gitignore', 'r') as f:
    print(line, end='')
    