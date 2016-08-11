#Diederique van der Knaap
#01/03/2015
#Computing GC Content

DNA = open('rosalind_gc.txt', 'r')
raw_samples = DNA.readlines()
DNA.close()

d = {}
cur_key = ''

for word in raw_samples:
    if word[0] == '>':
        cur_key = word[1:].rstrip()
        d[cur_key] = ''
    else:
        d[cur_key] += word.rstrip()

for s_id, s in d.iteritems():
    d[s_id] = (float(s.count('G') + s.count('C'))/len(s)*100)

(s_id, gc) = max(list(d.iteritems()), key = lambda item:item[1])
print s_id
print str(gc) + "%"




    


    
    
        
    
