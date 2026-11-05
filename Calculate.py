import sys
firstnumber = float(input('number?:'))
enzansiki = str(input('operator?(+, -, *, /):'))
if enzansiki not in ['+', '-', '*', '/']:
    print("error {} is not supported".format(b))
    sys.exit()
lastnumber = float(input('number?:'))
if enzansiki=='+':
    print(f'{firstnumber} + {lastnumber} = {firstnumber + lastnumber}')
elif enzansiki=='-':
    print(f'{firstnumber} - {lastnumber} = {firstnumber - lastnumber}')
elif enzansiki=='*':
    print(f'{firstnumber} * {lastnumber} = {firstnumber * lastnumber}')
elif enzansiki=='/':
    if lastnumber==0:
        print(f"error {firstnumber} / {lastnumber} is Can't calculate")
        sys.exit()
    print(f'{firstnumber} / {lastnumber} = {firstnumber / lastnumber}')
