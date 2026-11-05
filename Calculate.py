import sys
firstnumber = float(input('number?:'))
enzansiki = str(input('operator?(+, -, *, /):'))
if enzansiki not in ['+', '-', '*', '/']:
    print("error {} is not supported".format(b))
    sys.exit()
lastnumber = float(input('number?:'))
if enzansiki=='+':
    result = firstnumber + lastnumber
    print(result)
    print(f'{a} + {c} = {result}')
elif enzansiki=='-':
    result = firstnumber - lastnumber
    print(result)
    print(f'{a} - {c} = {result}')
elif enzansiki=='*':
    result = firstnumber * lastnumber
    print(result)
    print(f'{a} * {c} = {result}')
elif enzansiki=='/':
    if c==0:
        print(f"error {a} / {c} is Can't calculate")
        sys.exit()
    result = firstnumber / lastnumber
    print(result)
    print(f'{a} / {c} = {result}')
