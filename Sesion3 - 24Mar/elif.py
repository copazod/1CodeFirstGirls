t = float(input('Put the temperature: '))

if t>200:
    print ('too hot')
elif t<150:
    print('too cold')
elif t == 180:
    print('perfect t')
else:
    print('t close enough')