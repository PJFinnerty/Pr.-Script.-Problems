# Method one for writing a file

with open('w7myfile.txt', 'a') as f:
    print(f.tell())
    f.write("\nHello, from the line!")
    print(f.tell())
    