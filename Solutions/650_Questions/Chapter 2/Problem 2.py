
sum=0
answer = 'y'

while answer == 'y':

    number=int(input('Please Enter a Number:'))

    for i in range(number-1):
        
        if (number % (i+1))==0 :
            sum += i+1

    if sum == number :
        print('This number is Perfected')
    else :
        print('This number is Not Perfected')
    answer=input('Do you want to Continu (y/n):')


