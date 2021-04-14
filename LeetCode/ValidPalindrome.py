def isPalindrome(s: str):
    mystr = ""
    for i in s:
        if i.isalpha() or i.isnumeric():
            mystr += i.lower()
    if mystr != mystr[::-1]:
        return False
    return True

s = "abc,de,d,c,b,a"
res = isPalindrome(s)
print(res)
