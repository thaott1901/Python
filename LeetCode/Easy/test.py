import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...


def isSelfDescribing(n):
    s = str(n)
    for i, c in enumerate(s):
        if s.count(str(i)) != int(c):
            return False
    return True


for line in sys.stdin:
    res = isSelfDescribing(int(line))
    print(res, end="")



