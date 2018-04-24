friends = '''\
YYNN
YYYN
NYYN
NNNY'''.splitlines()


def join(data):
    while True:
        for tuple_, set1 in data.items():
            try:
                match = next(k for k, set2 in data.items() if k != tuple_ and set1 & set2)
            except StopIteration:
                # no match for this key - keep looking
                continue
            else:
                # merging match and set1
                data[tuple_] = set1 | data.pop(match)
                break
        else:
            # no match for any key - we are done!
            break


def friendCircles(friends):
    n = len(friends)

    data = {(i,): {i} for i in range(n)}
    for i, row in enumerate(friends):
        offset = row[i+1:]  # only iterate upper right triangle
        for j, elem in enumerate(offset, start=i+1):
            if elem == 'Y':
                data[i,j] = {i, j}

    join(data)
    circles = data.values()
    assert sorted(x for circle in circles for x in circle) == list(range(n))
    return len(circles)


print(friendCircles(friends))
