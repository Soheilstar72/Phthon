first_price=float(input('Please Enter the Pervious year price:'))
second_price=float(input('Please Enter the Current price:'))

increase=round((second_price/first_price - 1)*100)

new_price=second_price*second_price/first_price

print(f'The increase is equal to {increase} %')
print('Next year price will be equal to : ',new_price)