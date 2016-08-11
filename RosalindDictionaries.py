#12/31/2014
#This program takes a .txt file and outputs the different words and number of times they appear number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

d = {}
f = open('rosalind_ini6.txt', 'r')
f = f.read()
result = f.split()

for word in result:
      d[word]= str(result.count(word))
      
for key, value in d.items():
      print key, value
      
f = open('out.txt', 'w')


    

