## anagrams
w = ["eat", "tea", "tan", "ate", "nat", "bat"]
my_dict={}
for x in w:
    s = "".join(sorted(x))
    if s in my_dict:
        my_dict[s].append(x)
    else:
        my_dict[s]=[x]
print(my_dict)