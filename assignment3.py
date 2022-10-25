#Using the below as a starter code, complete the following for a program that accepts user input, writes info to a file, and then processes the info after reading it back. Before starting, create a plan, pseudocode, and version control strategy, and submit in a separate document. Within the program, write appropriate comments. 1001
file = open ( 'text.txt' , 'w' )



s = "Hello there\n"

  

file.write(s)

  

file.close()

 

file = open ( 'text.txt' , 'r' )



print (file.read())



file.close()