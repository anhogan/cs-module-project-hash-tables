def no_dups(s):
    if s == "":
        return ""

    # Set a hash to keep track of the words
    word_hash = {}

    sArr = s.split(" ")

    # Go through sArr and check each word
    for word in sArr:
        if word.lower() in word_hash:
            word_hash[word.lower()] += 1
        else:
            word_hash[word.lower()] = 1

    # Take each key in the hash and add it to an array
    single_string = list(word_hash.keys())
    single_string = ' '.join(single_string)

    return single_string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))