def numofBits(n):
    count=0
    while(n):
        count +=1
        n>>=1
    return count

n=int(input('Enter a number : '))
print('Nuber of bits :' , numofBits(n))