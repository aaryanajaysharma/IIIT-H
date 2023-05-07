# graph = [[2, 1, 1, 1, 1], [0, 1, 3, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 0, 1], [0, 0, 0, 0, 0]]
# start = [0,0]
# end = [1,2]

class Node:
    def __init__(self, i,j,d):
        self.row = i
        self.col = j
        self.distance = d
 
def BFS(grid,start):
    source = Node(start[0],start[1],0)

    visited = [[False for elem in range(len(grid[0]))]
               for elem in range(len(grid))]
     
    queue = []
    queue.append(source)
    visited[source.row][source.col] = True
    while len(queue) != 0:
        source = queue.pop(0)
 
        # Destination found;
        if (grid[source.row][source.col] == 3):
            return source.distance
 
        # moving up
        if checkValidity(source.row - 1, source.col, grid, visited):
            queue.append(Node(source.row - 1, source.col, source.distance + 1))
            visited[source.row - 1][source.col] = True
 
        # moving down
        if checkValidity(source.row + 1, source.col, grid, visited):
            queue.append(Node(source.row + 1, source.col, source.distance + 1))
            visited[source.row + 1][source.col] = True
 
        # moving left
        if checkValidity(source.row, source.col - 1, grid, visited):
            queue.append(Node(source.row, source.col - 1, source.distance + 1))
            visited[source.row][source.col - 1] = True
 
        # moving right
        if checkValidity(source.row, source.col + 1, grid, visited):
            queue.append(Node(source.row, source.col + 1, source.distance + 1))
            visited[source.row][source.col + 1] = True
 
    return -1
 
 
def checkValidity(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
        (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != 1) and (visited[x][y] == False)):
        return True
    return False



def isInRange(grid,x,y):
    if(x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] != 1):
        return True
    return False

def moveWithoutBreakingWalls(grid,start):
    row = start[0]
    col = start[1]
    options = {}

    if isInRange(grid,row-1,col):
        options[(row-1,col)] = BFS(grid,(row-1,col))
    if isInRange(grid,row+1,col):
        options[(row+1,col)] = BFS(grid,(row+1,col))
    if isInRange(grid,row,col-1):
        options[(row,col-1)] = BFS(grid,(row,col-1))
    if isInRange(grid,row,col+1):
        options[(row,col+1)] = BFS(grid,(row,col+1))

    final = {}

    for key in options:
        if options[key] != -1:
            final[key] = options[key]

    

    if len(final) == 0:
        return None

    # find key with min value
    for key in final:
        if final[key] == min(final.values()):
            return key
        


