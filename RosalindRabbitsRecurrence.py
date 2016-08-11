#Diederique van der Knaap
#01/02/2015
#Rabbits and Recurrence

#First, define the recurrence function
def recurrence(n, k):
    if n < 2:
        return n
    else:
        return (recurrence((n-1), k) + recurrence((n-2), k)*k)

#open file and convert to an array
f = open('rosalind_fib.txt', "r")
array = f.readlines()
rabbits = array[0].split()
n = int(rabbits[0])
k = int(rabbits[1])       

print recurrence(n, k)

