

def romanToInt(s: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_list = ("I", "V", "X", "L", "C", "D", "M")
    str_sum = 0
    subtract = 0
    for i in range(len(s)):
        a = s[i]
        index_a = roman_list.index(a)
        value_a = roman_dict.get(a)
        if i < len(s) - 1:
            b = s[i+1]
            index_b = roman_list.index(b)
            if index_a < index_b:
                subtract = value_a
                continue

        next_num = value_a - subtract
        str_sum += next_num
        subtract = 0
    return str_sum

def romanToInt1(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0
    for i in s[::-1]:
        if roman_dict[i] > prev:
            res += roman_dict[i]
        else:
            res -= roman_dict[i]
        prev = roman_dict[i]
    return res

s ="MCMXCIV"
result = romanToInt(s)
# print(result)

s1 = "MCMXCIV"
result1 = romanToInt1(s1)
print(result1)