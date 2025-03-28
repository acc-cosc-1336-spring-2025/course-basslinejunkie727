def Get_Hamming_Distance(str1,str2):
    #check if the strings are the same distance
    if len(str1)!=len(str2):
        raise ValueError('The DNA strings must be of the same length')
    #Initialize the accumulator 
    distance=0
    #loop through each character in the strings
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            distance+=1
    return distance

def Get_DNA_Compliment(dna):
    #define a dictionary for the compliments
    compliment={'A':'T','T':'A','C':'G','G':'C'}
    #create the reverse compliment
    reversed_compliment=''.join(compliment[base] for base in reversed(dna))
    return reversed_compliment