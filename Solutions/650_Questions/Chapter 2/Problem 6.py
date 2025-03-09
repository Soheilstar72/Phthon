birth=(map(int,input('Please Enter Your brith day (dd mm yy):').split(' ')))
now=(map(int,input('Please Enter currnt date (dd mm yy):').split(' ')))

bd,bm,by =birth
cd,cm,cy=now





if bd>cd :
    cd +=30
    cm -=1
if bm>cm :
    cm +=12
    cy -=1

dd=cd-bd
dm=cm-bm
dy=cy-by

day=dd+dm*30+dy*365

hour = day*24

min =hour *60

sec = min *60

print(f'Your old is {dy} years and {dm} months and {dd} days.')
print(f'You live {day} days or {hour} hours or {min} minutes or {sec} seconds')












