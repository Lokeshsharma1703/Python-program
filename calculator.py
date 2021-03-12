while True:
    n1=eval(input('Enter the first number : '))
    c=input('Enter sign of operation(+, -, *, /, %) : ')
    n2=eval(input('Enter the second number : '))
    if c in ('+','-','*','/','%'):
        if c=='+':
            print(f'{n1}+{n2} = ',n1+n2)
        elif c=='-':
            print(f'{n1}-{n2} = ',n1-n2)
        elif c=='*':
            print(f'{n1}*{n2} = ',n1*n2)
        elif c=='/':
            print(f'{n1}/{n2} = ',n1/n2)
        elif c=='%':
            print(f'{n1}%{n2} = ',n1%n2)
    else:
        print('Invalid operation number')
    print()
