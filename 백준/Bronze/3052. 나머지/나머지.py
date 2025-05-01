nlist = list()
for i in range(10):
    n = int(input())
    nlist.append(n%42)
print(len(list(set((nlist)))))