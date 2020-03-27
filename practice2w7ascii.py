#practice for writing to files
#Peter Finnerty

with open('w7mytext.txt', 'a') as f:
    print(f.tell())
    f.write("\nHello, from the line!")
    print(f.tell())