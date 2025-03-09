years=int(input("How many years do you need:"))
price=int(input('The Value of Service:'))
inflation = float(input('What is your forecast for inflation rate (%):'))

for i in range(years):
    price = price + price*inflation/100
    print(f'Price is equal to {price} in year {i+1}')