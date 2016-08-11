strand1 = raw_input("Enter the first DNA string: ")
strand2 = raw_input("Enter the second DNA string: ")

hamming_dist = 0

for index in range(len(strand1)):
    if strand1[index] != strand2[index]:
        hamming_dist +=1
print hamming_dist
        
