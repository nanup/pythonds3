from pythonds3.graphs import Graph, Vertex
from pythonds3.basic import Queue

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setPred(currentVert)
                nbr.setDistance(currentVert.getDistance() + 1)
                vertQueue.enqueue(nbr)
        currentVert.setColor('balck')

def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())