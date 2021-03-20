def canVisitAllRooms(rooms) -> bool:
    keys = []
    visited = []
    updated = True
    res = False
    if len(rooms) == 1:
        return updated
    for key in rooms[0]:
        keys.append(key)
    visited.append(0)
    while updated and not res:
        updated = False
        for i in range(1, len(rooms)):
            if i not in visited:
                if i in keys:
                    for key in rooms[i]:
                        keys.append(key)
                    updated = True
                    visited.append(i)
        if len(visited) == len(rooms):
            res = True
            break
        else:
            res = False
    return res


test = [[1,3],[3,0,1],[2],[0]]
res = canVisitAllRooms(test)
print(res)
