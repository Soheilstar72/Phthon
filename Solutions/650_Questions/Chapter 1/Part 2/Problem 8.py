number=int(input('Please Enter Number of Employees:'))

for i in range(number):
    idnumber=input("Please the employee's ID number:")
    hour=int(input('How many hours employee worked:'))
    fee = float(input('How much employee recive per hour:'))

    extra = 0

    if hour >40:
        extra=hour-40
        hour = 40
    
    salary = hour * fee + extra *fee *1.5

    print(f'The salary for employee with Id number {idnumber} is equal to {salary}')
    print(f'Employee should recive {hour *fee} as ordinary salary and {extra *fee *1.5} as extra hours')



















