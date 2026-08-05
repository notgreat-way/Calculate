#Copyright (C) 2026 2password
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
