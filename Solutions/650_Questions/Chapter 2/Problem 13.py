x,y=map(int,input('Please Enter two number : ').split(' '))

if x<0 or y<0:
    result='Error! at least one of you number is eaqual to 0'
else:
    sum=1
    for k in range(y):
        sum *= x
    result=(f'The result of {x} ^ {y} is equal to : {sum}')

print(result)