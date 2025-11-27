def printSubStrings(str):
    str_len = len(str)
    my_list=[]
    for i in range(str_len):
        for j in range(i,str_len):
            if str[i:j]:
                my_list.append(str[i:j])

    return list(set(my_list))

def distinct_substrings(s):
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.add(s[i:j])
    return result







# Driver code
if __name__ == '__main__':
    str = "aaabc"
    print(printSubStrings(str))
    # Example
    print(distinct_substrings("abc"))
    # {'a', 'b', 'c', 'ab', 'bc', 'abc'}