import sys
from pythonds3 import PriorityQueue, Graph, Vertex

def prim(aGraph, start):
    start.setDistance(0)
    for v in aGraph:
        v.setDistace(sys.maxsize)
        v.setPred(None)
    pq = PriorityQueue()
    pq.buildHeap([v.getConnections(), v] for v in aGraph)
    while not pq.isEmpty():
        currentV = v.delMin()
        for nextV in currentV.getConnections():
            newCost = currentV.getWeight(nextV)
            if nextV in pq and newCost < nextV.getDistance():
                nextV.setPred(currentV)
                nextV.setDistance(newCost)
                pq.decreaseKey(nextV, newCost)
