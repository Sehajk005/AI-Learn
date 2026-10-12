def pal(text):
    if len(text)<=1:
        return "Palindrome"
    else:
        if text[0]==text[-1]:
            return pal(text[1:-1])
        else:
            return "Not a Palindrome"