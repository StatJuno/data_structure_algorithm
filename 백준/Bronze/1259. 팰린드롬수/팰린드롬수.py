while 1:
    n = int(input())
    if n == 0 :
        break
    print('yes') if list(str(n)) == list(reversed(str(n))) else print('no')