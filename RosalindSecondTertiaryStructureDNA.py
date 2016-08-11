#Diederique van der Knaap
#01/02/2015
#This program takes a DNA string S of length at most 1000 bp and returns the reverse complement s^c of s

DNA_String = open('rosalind_revc.txt', 'r')
DNA_String = list(DNA_String.read())

reverse_string = DNA_String[::-1]
for n, i in enumerate(reverse_string):
    if i == 'A':
        reverse_string[n]='T'
    elif i == 'T':
        reverse_string[n] = 'A'
    elif i == 'C':
        reverse_string[n] = 'G'
    elif i == 'G':
        reverse_string[n] = 'C'

complement = ''.join(reverse_string)
print complement
