import util

def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

def findNeib(maze, currentindex):
    listNeib = []
    currentI = currentindex[0]
    currentJ = currentindex[1]
    formerI = currentI-1
    laterI = currentI+1
    formerJ= currentJ-1
    laterJ = currentJ+1
    if maze[formerI][currentJ] != True:
        listNeib.append((formerI, currentJ))
    if maze[currentI][formerJ] != True:
        listNeib.append((currentI, formerJ))
    if maze[laterI][currentJ] != True:
        listNeib.append((laterI, currentJ))
    if maze[currentI][laterJ] != True:
        listNeib.append((currentI, laterJ))
    return listNeib

def astar(maze, startindex, endindex):
    minpath = {str(startindex): 0}
    priorityQueue = util.PriorityQueue()
    priorityQueue.push(startindex, 0)
    while True:
        try:
            node = priorityQueue.pop()
        except Exception:
            return minpath[str(endindex)]
        listNeib = findNeib(maze, node)
        for neib in listNeib:
            if str(neib) not in minpath:
                minpath[str(neib)] = minpath[str(node)] + 1
            elif minpath[str(neib)] > minpath[str(node)] + 1:
                minpath[str(neib)] = minpath[str(node)] + 1
            else:
                continue
            if str(neib) == str(endindex):
                continue
            estimation = minpath[str(neib)] + manhattanDistance(neib, endindex)
            priorityQueue.push(neib, estimation)


def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    graph = []
    graphMap = {}
    sumNode = {}
    visited = {}
    for i in range(1, g_nodes + 1):
        graphMap[i] = []
        visited[i] = False
        sumNode[i] = 0
    for i in range(len(g_from)):
        graph.append([g_weight[i], g_from[i], g_to[i]])
    sortedGraph = sorted(graph)
    sumAllNode = 0
    listSetNode = []
    for e in sortedGraph:
        ii1 = 0
        i1 = -1
        for setNode in listSetNode:
            if e[1] in setNode:
                i1 = ii1
            ii1 += 1
        ii2 = 0
        i2 = -1
        for setNode in listSetNode:
            if e[2] in setNode:
                i2 = ii2
            ii2 += 1
        if i1 == -1 and i2 == -1:
            listSetNode.append({e[1], e[2]})
            sumAllNode += e[0]
        elif i1 == -1 and i2 >= 0:
            listSetNode[i2].add(e[1])
            sumAllNode += e[0]
        elif i2 == -1 and i1 >= 0:
            listSetNode[i1].add(e[2])
            sumAllNode += e[0]
        elif i1 >= 0 and i2 >= 0 and i1 != i2:
            # print(i1)
            # print(i2)
            newset = list(listSetNode[i1]) + list(listSetNode[i2])
            listSetNode.pop(max(i1, i2))
            listSetNode.pop(min(i1, i2))
            listSetNode.append(set(newset))
            sumAllNode += e[0]
        # print(listSetNode)
    return sumAllNode


def prims(n, edges, start):
    graph = {}
    visited = {}
    listVisited = set()
    for i in range(0, n):
        graph[i] = []
        visited[i] = False
    for e in edges:
        graph[e[0]].append([e[0], e[1], e[2]])
        graph[e[1]].append([e[1], e[0], e[2]])

    listPath = graph[start]

    sumPath = 0

    def popMinPath():
        if len(listPath) == 0:
            raise Exception
        minPath = listPath[0]
        minIndex = 0
        for i in range(len(listPath)):
            if listPath[i][0] in listVisited and listPath[i][1] in listVisited:
                continue
            if listPath[i][2] < minPath[2]:
                minPath = listPath[i]
                minIndex = i
        if len(listPath) == 0:
            raise Exception
        listPath.pop(minIndex)
        return minPath

    while True:
        for path1 in listPath:
            # print(path1[0])
            # print(path1[1])
            # print(listVisited)
            if path1[0] in listVisited and path1[1] in listVisited:
                listPath.remove(path1)
        # print(listPath)
        if len(listVisited) == n:
            break
        try:
            path = popMinPath()
        except Exception as e:
            # print(str(e))
            break
        sumPath += path[2]
        if path[0] not in listVisited:
            listPath = listPath + graph[path[0]]
            listVisited.add(path[0])
        if path[1] not in listVisited:
            listPath = listPath + graph[path[1]]
            listVisited.add(path[1])
        # print(listVisited)
        # print(sumPath)
    return sumPath


