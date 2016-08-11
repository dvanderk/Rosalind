#Diederique van der Knaap
#01/01/2015
#This program takes a .txt file of a DNA string s of length at most 1000 nt and outputs four integers seperatd by spaces counting the respective 

d = {}
DNA_String = open('rosalind_dna.txt', 'r')
DNA_String = DNA_String.read()

for word in DNA_String:
      d[word]= str(DNA_String.count(word))
      
print d['A'], d['C'], d['G'], d['T']
      
f = open('out.txt', 'w')


##d = {}
##DNA_String = open('rosalind_dna.txt', 'r')
##DNA_String = DNA_String.read()
##
##count_A = 0
##count_C = 0
##count_G = 0
##count_T = 0
##
##for letter in DNA_String:
##    if letter == 'A':
##        count_A = count_A +1
##    if letter == 'C':
##        count_C = count_C +1
##    if letter == 'G':
##        count_G = count_G +1
##    if letter == 'T':
##        count_T = count_T +1
##
##d['A']= str(count_A)
##d['C'] = str(count_C)
##d['G'] = str(count_G)
##d['T'] = str(count_T)
##
##print d['A'], d['C'], d['G'], d['T']
##
##f = open('out.txt', 'w')



#Below is a simpler way that I found on stackexchange using dictionary.get(), which allows you to supply a default value for missing keys

##for c in DNA_String:
##    d[c] = d.get(c, 0) + 1
##
##print d['A'], d['C'], d['G'], d['T']
