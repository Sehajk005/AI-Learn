def leap_year(n):
    if n%4==0:
        return True
    else:
        return False

n = int(input("Enter a Year: "))
print(leap_year(n))