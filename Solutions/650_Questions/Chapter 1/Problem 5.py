import math
velocity=float(input('Please Enter the ind Speed in km/h:'))
temperature=float(input('Please Enter the air temperature in Degree Celsius:'))

wci=13.12+0.6215*temperature-11.37*math.pow(velocity,0.16)+0.3965*temperature*math.pow(velocity,0.16)


print('The wind chill index is equal to %i' %int(round(wci,0)))
