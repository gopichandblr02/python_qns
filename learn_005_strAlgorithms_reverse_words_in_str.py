def reverse_words(st):
    a=[x for x in st.split(".") if x]
    a.reverse()
    return ' '.join(a)

def reverse_words_otherway(st):
    a=st.split(".")
    my_list=[]
    for x in a:
        if x:
            my_list.append(x)
    my_list.reverse()
    return ' '.join(my_list)


if __name__ == "__main__":
    str = "..geeks..for.gopi."
    print(reverse_words(str))
    print(reverse_words_otherway(str))