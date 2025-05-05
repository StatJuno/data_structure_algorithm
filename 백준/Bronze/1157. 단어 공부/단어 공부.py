words = input().upper()
words_list = list(set(words))
result = list()
for i in words_list:
    letter = words.count(i)
    result.append(letter)
        
if result.count(max(result)) >= 2:
    print("?")
else:
    print(words_list[result.index(max(result))])