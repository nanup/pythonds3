from pythonds3 import Graph, PriorityQueue, Vertex

def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistance = 0
    pq.buildHeap([(x.getDisatnce(), x)] for x in aGraph)
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)