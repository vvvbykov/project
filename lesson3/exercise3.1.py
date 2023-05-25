words = 'Hello word'
s = words.split()
print('!', s[1], '!', s[0], '!')
print(f'! {s[1]} ! {s[0]} !')
print('! {var1} ! {var2} !'.format(var1=s[1], var2=s[0]))