words = input()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian:
    words = words.replace(i, '#')
print(len(words))