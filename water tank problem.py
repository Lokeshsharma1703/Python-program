h=eval(input('Enter the height of tank : '))
r=eval(input('Enter the radius of tank : '))
f=eval(input('Enter the flow rate of water : '))
t=eval(input('Enter the time : '))
v=3.14*r**2*h
vw=f*t
if vw>v:
    print('Over flow')
    print('Volume = ',vw-v)
elif vw==v:
    print('Tank full')
else:
    print('Under flow')
    ht=vw/(3.14*r**2)
    hr=h-t
    print(f'filled height {ht} and remaining height {hr}')
