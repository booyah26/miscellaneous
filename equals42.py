# Code I created for a job interview question
# Q.4 of 4
# If given a string of 5 random numbers, can any permutation of those using +,-,* equal 42

import sys
import itertools as it
import operator

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}
for line in sys.stdin:

    #Initialise possible variable to be default "NO"
    possible = "NO"
    #Split the stdin input into a list, by blank space. Results is in strings not integers here
    results = line.split(' ')
    
    #for loop to convers results from strings to integers
    for i in range(len(results)):
        results[i] = int(results[i])
    
    #create array with four of each +, -, *. This allows for four of each operand for each arrangement of cards    
    ops = ['*','+','-','*','+','-','*','+','-','*','+','-']
    
    #Use itertools.permutations to calculate all possible arrangements
    permuted = list(it.permutations(results, 5))
    oppermuted = list(it.permutations(ops, 4))
    
    #create array variable for for loops
    #variable could be removed by substituting i[]'s with operatorlookup or permuted variable direct in the for loops, however this looks neater
    i = [0] * 9


    for x in range(len(oppermuted)):

        i[1] = operatorlookup.get(oppermuted[x][0])
        i[3] = operatorlookup.get(oppermuted[x][1])
        i[5] = operatorlookup.get(oppermuted[x][2])
        i[7] = operatorlookup.get(oppermuted[x][3])
        for y in range(len(permuted)):
          
            i[0] = permuted[y][0]
            i[2] = permuted[y][1]
            i[4] = permuted[y][2]
            i[6] = permuted[y][3]
            i[8] = permuted[y][4]


            v1 = i[1](i[0],i[2])
            v2 = i[3](v1,i[4])
            v3 = i[5](v2,i[6])
            v4 = i[7](v3,i[8])

            
            if v4 == 42:
                possible = "YES"
        
    print(possible, end="")
