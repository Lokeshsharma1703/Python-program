ch=input('Enter a character : ')
if ch>='A' and ch<='Z':
    print('Upper case')
elif ch>='a' and ch<='z':
    print('Lower case')
elif ch>='0' and ch<='9':
    print('Digit')
else:
    print('Special Character')
