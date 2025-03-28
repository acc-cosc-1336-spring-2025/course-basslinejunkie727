def Get_Hamming_Distance(str1,str2):
    #check if the strings are the same length
    if len(str1)!=len(str2):
        raise ValueError('The DNA strings must be of the same length')
    #Initialize the accumulator 
    distance=0
    #loop through each character in the strings
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            distance+=1
    return distance

def Get_DNA_Complement(dna):
    #define a dictionary for the complements
    complement={'A':'T','T':'A','C':'G','G':'C'}
    #create the reverse compliment
    reversed_complement=''.join(complement[base] for base in reversed(dna))
    return reversed_complement

def main():
    while True:
        print('Menu:')
        print('1. Hamming Distance')
        print('2. DNA complement')
        print('3. Exit')
        #Get user choice
        choice=input('Choose an option (1/2/3)')

        if choice== '1':
            #option 1 Hamming Distance
            str1=input('input the first DNA string')
            str2=input('input the second DNA string')
            try:
                distance=Get_Hamming_Distance(str1,str2)
                print(f'Hamming Distance:{distance}')
            except ValueError as e:
                print(e)
        
        elif choice== '2':
            #option 2 DNA complement
            dna=input('enter the DNA string:')
            complement= Get_DNA_Complement(dna)
            print('Reverse Complement: {complement}')

        elif choice== '3':
            #option 3 exit
            print('Exiting the program')
        
        else:
            print('Please choose a valid option')
main()
