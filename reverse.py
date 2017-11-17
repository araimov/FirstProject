def reverse(text):
    new_string = ""
    rev_length = len(text) - 1
    while rev_length >= 0:
        new_string = new_string + text[rev_length]
        rev_length -= 1
    return new_string


print (reverse('abcd'))