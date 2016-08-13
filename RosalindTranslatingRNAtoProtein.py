## Rosalind Bioinformatics Stronghold: Translating RNA to Protein
## Dee van der Knaap
## Last Edited 08/13/16


RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def main():
        
    protein = ""
    RNA_file = 'rosalind_prot.txt'
    with open(RNA_file) as f:
        RNA_seq = f.read()
    #RNA_seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'


    while len(RNA_seq) > 2:
        codon = RNA_seq[0:3]
        if codon != 'AUG':
            RNA_seq[2:]
        else:
            coding_region = RNA_seq
            break

    while len(coding_region) > 2:
        codon = coding_region[0:3]
        print codon
        amino_acid = RNA_CODON_TABLE[codon]
        if amino_acid != 'Stop':
            protein += amino_acid
            coding_region = coding_region[3:]
        else:
            break
    print protein
   
            


if __name__ == '__main__':
    main()
    
