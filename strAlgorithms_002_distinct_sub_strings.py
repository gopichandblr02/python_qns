def printSubStrings(str):
    str_len = len(str)
    my_list=[]
    for i in range(str_len):
        for j in range(i,str_len):
            if str[i:j]:
                my_list.append(str[i:j])

    return list(set(my_list))




# Driver code
if __name__ == '__main__':
    str = "aaabc"
    print(printSubStrings(str))