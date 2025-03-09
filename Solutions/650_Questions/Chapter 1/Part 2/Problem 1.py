number=int(input('Please Enter the Number of student:'))

while number<2 :
    number=int(input('Warning!!! Please Enter a Number greater than 1:'))

max1=0.0

max2=0.0

id1=0
id2=0


for i in range (1,number+1):

    avreage=float(input(f'Please enter the avrage of student number {i} : '))
    while avreage<=0:
       avreage=float(input('Warning!!! Please Enter a Number greater than 0:'))
    
    if avreage > max1 :
        max2=max1
        max1=avreage
        id2=id1
        id1=i
        max1=avreage
        id1=i

    else:
        if avreage > max2:
            max2=avreage
            id2=i


print('The second grade is for student number',id2 , ' with grade ',max2)