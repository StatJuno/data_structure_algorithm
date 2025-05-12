word = str(input())

for i in word:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    print(i, end='')