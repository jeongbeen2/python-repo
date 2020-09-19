def is_palindrome(word):
    list_word = list(word)

    if list_word[0] == list_word[-1]:
        if list_word[1] == list_word[-2]:
            if list_word[2] == list_word[-3]:
                print(True)
            else:
                print(False)
    return list_word


print(is_palindrome("raccecar"))

print("test!")