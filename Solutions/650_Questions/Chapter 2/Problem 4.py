text = input('Please Enter your text: ')
new=''

for i in text:
    if i != ' ':
        new = new + i + ' '
    else :
        new += i


print(new)




