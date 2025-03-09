number=input('Please Enter your number : ')

n = len(number)

quality= 'YES, It is a Pefect Number'

for i in range(n//2) :
    if number[i] != number[-i-1]:
        quality='NO, It is not a Perect Number'

print(quality)