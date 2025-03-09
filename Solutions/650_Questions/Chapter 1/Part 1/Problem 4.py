from math import  tan,pi

number=int(input('Please Enter the number of sides:'))
side=float(input('Please Enter the length of sides:'))

area= (number*(side*side))/(4*tan(pi/number))

print('the Area is equal to %f' %area)

