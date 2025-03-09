answer = 'y'

while answer== 'y' :
    need = int(input('Please Enter How much do yo need: '))
    number = int(input('Please Enter How many Installment do yo want to Pay: '))
    fee = float(input('Please Enter Interest rate: '))
    total=(12*need)/(12-number*fee/100)
    each=total/number

    print(f'You should pay {total} and in each time you should pay {each}')
    answer=input('Do you want to continu (y/n): ')
