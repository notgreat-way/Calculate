import sys
a = float(input('number?:'))
b = str(input('operator?(+, -, *, /):'))
if b not in ['+', '-', '*', '/']:
    print("error {} is not supported".format(b))
    sys.exit()
c = float(input('number?:'))
if b=='+':
    result = a + c
    print(result)
    print(f'{a} + {c} = {result}')
elif b=='-':
    result = a - c
    print(result)
    print(f'{a} - {c} = {result}')
elif b=='*':
    result = a * c
    print(result)
    print(f'{a} * {c} = {result}')
elif b=='/':
    if c==0:
        print(f"error {a} / {c} is Can't calculate")
        sys.exit()
    result = a / c
    print(result)
    print(f'{a} / {c} = {result}')