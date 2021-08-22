def insert(intervals, newInterval):
    left = []
    right = []
    mid = []
    start, end = newInterval[0], newInterval[1]
    for i in intervals:
        if i[1] < newInterval[0]:
            left.append(i)
        elif i[0] > newInterval[1]:
            right.append(i)
        else:
            start = min(i[0], start)
            end = max(i[1], end)
    mid.append([start, end])
    return left + mid + right


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
res = insert(intervals, newInterval)
print(res)
