salary=float(input('Please enter your salary:'))

insurance =round(0.07 * salary)
tax = round(0.1 * salary)

income = salary - insurance - tax

print('Your salary is equal to :' , salary,
    '\n Your insurance is equal to :' , insurance  ,
    '\n Your tax is equal to :' , tax ,
    '\n Your income is equal to :' , income)