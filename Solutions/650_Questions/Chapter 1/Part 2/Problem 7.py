numbers=map(int,input('Please Enter Three numbers (1st 2nd 3rd):').split(' '))

first , second , third = numbers

if first > second and first > third :
    big = first
    if second > third :
        medium= second
        small = third
    else :
        medium=third 
        small = second
elif second>first and second>third :
    big = second
    if first > third :
        medium= first
        small = third
    else :
        medium=third 
        small = first

else:
    big = third
    if first > second :
        medium= first
        small = second
    else :
        medium=third
        small = second

print (f'{small} , {medium} , {big}')





