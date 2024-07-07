from heapq import heapify, heappop

def findSet(x):
    if union_set_list[x][0] == x:
        return x
    else:
        return findSet(union_set_list[x][0])

def unionSet(i, j):
    x = findSet(i)
    y = findSet(j)

    if x != y:
        union_set_list[x][0] = y
        union_set_list[y][1] += union_set_list[x][1]

def heapSort(graph, edges):
    new = []

    for x in range(edges):
        heapify(graph)
        new.append(heappop(graph))

    return new

def krushkal(edges, minimum):
    sorted_array = heapSort(edges, int(first[1]))

    for i in sorted_array:
        x = findSet(i[2])
        y = findSet(i[1])
        if x != y:
            unionSet(i[2], i[1])
            minimum += i[0]

    return minimum


read_list = [["input2a.txt", "output2a.txt"], ["input2b.txt", "output2b.txt"]]

for num in read_list:
    r = open(num[0], 'r')
    w = open(num[1], 'w')

    first = r.readline().split()

    union_set_list = []
    for x in range(int(first[0]) + 1):
        union_set_list.append([x, 1])

    list = []
    for y in range(int(first[1])):
        second = r.readline().split()
        second = [int(x) for x in second]
        reverse = second[::-1]
        list.append(reverse)

    minimum = krushkal(list, 0)

    output = f"{minimum}"
    w.write(output)
    w.close()









