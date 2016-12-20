import re


class Maze():

    def __init__(self):
        self.grid  = [[1,1,1,1,1,1,1,1],
                      [1,0,0,0,0,0,1,1],
                      [1,1,1,0,0,0,1,1],
                      [1,0,0,0,1,0,0,1],
                      [1,0,1,1,0,0,1,1],
                      [1,0,1,0,0,1,0,1],
                      [1,0,1,0,0,0,2,1],
                      [1,1,1,1,1,1,1,1]]

    def search(self,x,y):
        if self.grid[x][y] == 2:
            print 'found at %d,%d' % (x, y)
            return True
        elif self.grid[x][y] == 1:
            print 'wall at %d, %d' % (x, y)
            return False
        elif self.grid[x][y] == 3:
            print 'visited at %d, %d' % (x, y)
            return False

        print 'visiting %d, %d' % (x, y)

        # mark as visited
        self.grid[x][y] = 3

        # explore neighbors clockwise starting by the one on the right
        if ((x < len(self.grid)-1 and search(x+1, y))
                or (y > 0 and search(x, y-1))
                or (x > 0 and search(x-1, y))
                or (y < len(self.grid)-1 and search(x, y+1))):
            return True
        
        return False

    def exportgrid(self,filename='maze'):
        positions = ''
        for x in self.grid:
            for y in x:
                positions += str(y)
            positions += '\n'

        positions = self.num_to_ascii(positions)

        # write to file
        f = open(filename, 'w')
        f.write(positions)
        f.close

    def importgrid(self,filename='maze'):
        self.grid = []
        with open(filename, 'r') as f:
            for line in f:
                xposition = self.ascii_to_num(line)
                newlist = list(xposition)
                newlist = [x for x in newlist if x != '\n']
                self.grid.append(newlist)
        
        self.grid = [x for x in self.grid if x != []]
        
    def ascii_to_num(self, positions):
        positions = re.sub(' ', '0', positions)
        positions = re.sub('#', '1', positions)
        positions = re.sub('X', '2', positions)
        positions = re.sub('\.', '3', positions)
        return positions

    def num_to_ascii(self, positions):
        'draw in a more visible way'
        positions = re.sub('0', ' ', positions)
        positions = re.sub('1', '#', positions)
        positions = re.sub('2', 'X', positions)
        positions = re.sub('3', '.', positions)
        return positions
        
if __name__ == '__main__':
    search(1, 1)
