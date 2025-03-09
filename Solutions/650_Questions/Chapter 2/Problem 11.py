x,y=map(int,input('Please Enter two number : ').split(' '))

i=1
j=1

m=x
n=y


if y<0:
    i=-1
    y=abs(y)
if x<0:
    j=-1
    x=abs(x)


if x==0 or y==0:
    result='Error! at least one of you number is eaqual to 0'
else:
    sum=0
    for k in range(x):
        sum += y
    result=(f'The result of {m} * {n} is equal to : {sum*i*j}')

print(result)

        




