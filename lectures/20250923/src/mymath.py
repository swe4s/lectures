import sys
import math_lib

opp = sys.argv[1]
p1 = sys.argv[2]
p2 = sys.argv[3]


if opp == 'add':
    print(math_lib.add(int(p1), int(p2)))
elif opp == 'div':
    try:
        print(math_lib.div(int(p1), int(p2)))
    except ZeroDivisionError:
        print("Error: Division by zero")
        sys.exit(1)

