import math
d = 0
pi=math.pi
while True:
    try:
      d=float(input("what is the diameter\n"))/2
      if d<0:
        print('please enter a positive number')
        continue
        
    except ValueError:
        print("Please enter a number")
        continue
      
    else:
        pi = math.pi
        c = 2 * pi * d
        a = pi * (d ** 2)
        print('circumference = ',c)
        print('area = ',a)
        break
