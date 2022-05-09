from pythonds3.graphs import Graph

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nId = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nId)
    return ktGraph

def posToNodeId(row, col, board_size):
    return (row * board_size) + col

def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   ( 1, -2), ( 1, 2), ( 2, -1), ( 2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

def knightTour(current_depth, vertex_list, current_vertex, node_limit):
    current_vertex.set_color('gray')
    vertex_list.append(current_vertex)
    if current_depth < node_limit:
        nbrList = list(current_vertex.orderByAvail(current_vertex))
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(current_depth + 1, vertex_list, nbrList[i], node_limit)
                I += 1
        if not done:
            vertex_list.pop()
            current_vertex.setColor('white')

    else:
        done = True

    return done

def orderByAvail(current_vertex):
    resList = []
    for vertex in current_vertex.getConnections():
        if vertex.getColor() == "white":
            c = 0
            for connection in vertex.getConnections():
                if connection.getColor() == 'white':
                    c += 1
            resList.append((c, connection))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]