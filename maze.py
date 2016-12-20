import re
grid  = [[1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,1,1],
         [1,1,1,0,0,0,1,1],
         [1,0,0,0,1,0,0,1],
         [1,0,1,1,0,0,1,1],
         [1,0,1,0,0,1,0,1],
         [1,0,1,0,0,0,2,1],
         [1,1,1,1,1,1,1,1]]

def search(x,y):
    if grid[x][y] == 2:
        print 'found at %d,%d' % (x, y)
        return True
    elif grid[x][y] == 1:
        print 'wall at %d, %d' % (x, y)
        return False
    elif grid[x][y] == 3:
        print 'visited at %d, %d' % (x, y)
        return False

    print 'visiting %d, %d' % (x, y)

    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y))
            or (y > 0 and search(x, y-1))
            or (x > 0 and search(x-1, y))
            or (y < len(grid)-1 and search(x, y+1))):
        return True
    
    return False

def exportgrid(filename='maze'):
    positions = ''
    for x in grid:
        for y in x:
            positions += str(y)
        positions += '\n'

    positions = num_to_ascii(positions)

    # write to file
    f = open(filename, 'w')
    f.write(positions)
    f.close

def importgrid(filename='maze'):
    newgrid = []
    with open(filename, 'r') as f:
        for line in f:
            xposition = ascii_to_num(line)
            print xposition
            newlist = list(xposition)
            newgrid.append(newlist)
    grid = newgrid




def ascii_to_num(positions):
    positions = re.sub(' ', '0', positions)
    positions = re.sub('#', '1', positions)
    positions = re.sub('X', '2', positions)
    positions = re.sub('\.', '3', positions)
    return positions

def num_to_ascii(positions):
    'draw in a more visible way'
    positions = re.sub('0', ' ', positions)
    positions = re.sub('1', '#', positions)
    positions = re.sub('2', 'X', positions)
    positions = re.sub('3', '.', positions)
    return positions
    
if __name__ == '__main__':
    search(1, 1)
