number=int(input('Please Enter the Number of sentence you want:'))

a1=1
a2=2

if number==1:
    answer = a1
elif number == 2:
    answer = a2
else :
    print(a1)
    print(a2)
    i=3
    while i<=number:
        a3=a2+a1
        print(a3)
        a1 =a2
        a2 = a3
        i += 1
