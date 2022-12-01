def index_of_caps(word):
    list_caps = []
    for i in range(len(word)):
        if word[i].isupper():
            list_caps.append(i)
    return list_caps

