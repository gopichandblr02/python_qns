def reverse_words(st):
    a=[x for x in st.split(".") if x]
    a.reverse()
    return ' '.join(a)

if __name__ == "__main__":
    str = "..geeks..for.gopi."
    print(reverse_words(str))