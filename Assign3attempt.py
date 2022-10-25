#Using the below as a starter code, complete the following 
#for a program that accepts user input, writes info to a file, 
#and then processes the info after reading it back. Before starting, 
#create a plan, pseudocode, and version control strategy, 
#and submit in a separate document. Within the program, 
#write appropriate comments. 1001

#opening/creating txt.txt
file = open ( 'text.txt' , 'w' )



s = input("Hello there\n")
c = input("My name is Andre Graham\n")
h = input("I'm studying informatics\n")
o_o = input("Programming is getting increasingly fun\n")
l = input("And I'm beginning to understand more, and more, as I practice.\n")
  

file.write(s)
file.write(c)
file.write(h)
file.write(o_o)
file.write(l)

file.close()


 

file = open ( 'text.txt' , 'r' )



print (file.read())



file.close()