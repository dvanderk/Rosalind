### Rosalind FindMotif.py
### Dee van der Knaap
### Date Edited: 08/13/16

##Input: Two strings of DNA s and t, where t is a substring of s
##Output: All location of t in s


def main():

    #s = raw_input("Please enter the DNA string: ")
    #t = raw_input("Please enter the motif: ")

    motif_file = 'rosalind_subs.txt'
    with open(motif_file) as f:
        DNA_and_motif = f.read().split('\n')

    s = DNA_and_motif[0] #DNA
    t = DNA_and_motif[1] #motif

    index = 1

    while len(s) > 0:
        #print s[0:len(t)] 
        if s[0:len(t)] == t:
            print index
            index += 1
        else:
            index += 1
        s = s[1:]

if __name__ == '__main__':
    main()
        
