def isValid(s: str) -> bool:
    dict = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in s:
        if i in dict:
            top_stack = stack.pop() if stack else '#'
            if dict[i] != top_stack:
                return False
        else:
            stack.append(i)
    return not stack

st = "()[]{}"
res = isValid(st)
print(res)


