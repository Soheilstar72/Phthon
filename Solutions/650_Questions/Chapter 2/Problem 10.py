x=float(input("Please Enter the x : "))

sum=0
j=0
den = 0

for i in range(1,11):
    den=den+i*pow(x,i)
    j=pow(-1,i+1)
    sum=sum+j/den

print('The answer is equal to : ',sum)
    