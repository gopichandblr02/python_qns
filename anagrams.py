### Using dictionary
w = ["eat", "tea", "tan", "ate", "nat", "bat"]
a={}
for word in w:
    s = ''.join(sorted(word))
    print(s,type(s))
    if s in a:
        a[s].append(word)
    else:
        a[s]=[word]
print(a)   # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
