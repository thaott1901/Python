# num1 = input("Input num1: ")
# num2 = input("Input num2: ")
# result = float(num1) + float(num2)
# print(result)

# list ----------------------------------------------------------
print("\nList section: ")
friends = ["Abc", "B", "C", "D", "E"]
nums = [2, 4, 9, 15, 25, 36]
print(friends[0:])
friends.extend(nums)
print(friends)
friends.remove(9)
friends.append(13)
print(friends)
print(friends.count(2))
friends2 = friends.copy()
print(friends2)

# Tuples ----------------------------------------------------------
print("\nTuples section: ")
coor = [(4, 5), (1, 2)]
coor[0] = (8, 9)
print(coor[0][0])


# Function ----------------------------------------------------------
print("\nFunction section: ")


def say_hi(param):
    print("Hello World " + param)


print("Top")
say_hi(friends[2])
print("Bottom")


def cube(number):
    return pow(number, 3)


print("Cube of 3 is: " + str(cube(3)))

# If ----------------------------------------------------------
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are male")
elif is_male and not is_tall:
    print("Short male")
elif not is_male and is_tall:
    print("Not a male, but tall")
else:
    print("Not male, not tall")


# +++++++++++++++++++++++++  max_num +++++++++++++++++++++++++
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num("a", "cC", "c"))

# +++++++++++++++++++++++++  simple calculator +++++++++++++++++++++++++
# num1 = float(input("Input num1: "))
# op = input("Input op: ")
# num2 = float(input("Input num2: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("invalid op")

# +++++++++++++++++++++++++  dictionary +++++++++++++++++++++++++
months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}
print(months.get("Jana", "Invalid key"))

# +++++++++++++++++++++++++  While loop +++++++++++++++++++++++++
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")
# +++++++++++++++++++++++++  for loop +++++++++++++++++++++++++
for letter in "ABCDE FG HIJK LMN OP":
    print(letter)

for num in range(5, 10):
    print(num)

print("--------------------- exponent function -------------------------")


# +++++++++++++++++++++++++  exponent function +++++++++++++++++++++++++
def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))

print("--------------------- 2D list and nested loop -----------------------")


# +++++++++++++++++++++++++  2D list and nested loop +++++++++++++++++++++++++
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])
print(number_grid[0])
for row in number_grid:
    for col in row:
        print(col)

print("--------------------- Catching error -----------------------")


# +++++++++++++++++++++++++  Catching error +++++++++++++++++++++++++
try:
    # value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)