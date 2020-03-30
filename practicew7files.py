#Peter Finnerty

#Method 1 for opening files:


with open('slow.txt', 'r') as file:
    lines = file.readlines()
    upper = 0
    lower = 0

    for line in lines:
        line = line.strip( )
        if line.find("E") != -1:
            upper = upper + 1
        if line.find("e") != -1:
            lower = lower + 1

    print("Number of uppercase E's: ", upper)
    print("Number of lowercase e'sL: ", lower)

# https://www.youtube.com/watch?v=1uA-pLITer0
    
#with open('slow.txt', 'r') as f:
    #for i in range(101, 102):
     #   print(f" {chr(i)}")
    

#with open('slow.txt', 'r') as f:
  ##  for i in range(101, 101):
        #print(f"{i:3} {i:08b} {chr(i)}")