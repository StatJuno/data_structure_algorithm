L = int(input())
string = input()
hash = 0

for i in range(L):
    hash += (ord(string[i]) - 96) * (31 ** i)
    
print(hash % 1234567891)