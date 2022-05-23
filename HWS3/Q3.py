
year = input('Which year is the book?')
c = year[0:2]
d = year[2]
#print(c)
#print(d)
if c == '18':
    cent = ('19th century, ')

elif c =='19':
    cent = '20th century, '

if d == '7':
    dec = ('seventies')
elif d == '6':
    dec = ('sixties')
elif d == '5':
    dec = ('fifties')
elif d == '4':
    dec = ('40s')
elif d == '3':
    dec = ('30s')
elif d == '2':
    dec = ('20s')
elif d == '1':
    dec = ('10s')
elif d == '8':
    dec = ('80s')
elif d == '9':
    dec = ('90s')

print(cent,dec)