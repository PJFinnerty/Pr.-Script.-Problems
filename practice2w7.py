#Peter Finnerty

#f = open("moby-dick.txt", "r")
#print(f.read())

#f = close()

#string1 = 'slow.txt'.count('w')
#print(string1)



with open('slow.txt', 'r') as f:

    size_to_read = 2
    
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(4)

    f_contents = f.read(size_to_read)
    print(f_contents)

    #print(f.tell())

    #while len(f_contents) > 0:
       # print(f_contents, end='*')
        #f_contents = f.read(size_to_read)


   

#data = infile.read( )
#numofch = len(data)
#print(numofch)

#infile.close()
   
  

 #https://www.youtube.com/watch?v=szIFFw_Xl_M