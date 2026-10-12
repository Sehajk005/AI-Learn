n = int(input("Enter a 4 digit num"))
str_n = str(n)
reverse_n_str = str_n[::-1]
reverse_n = int(reverse_n_str)
print(reverse_n)
def pal(n):
    if n == reverse_n:
        return True
    else:
        return False
print(pal(n))