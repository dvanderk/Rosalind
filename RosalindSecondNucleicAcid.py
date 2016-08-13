#Diederique van der Knaap
#01/02/2015
#This program transcribes a DNA strand t having length at most 1000 nt into a RNA string/

DNA_String = open('rosalind_rna.txt', 'r')
DNA_String = DNA_String.read()

RNA_String = str.replace(DNA_String, 'T', 'U')
print RNA_String


    

