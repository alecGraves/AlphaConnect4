import numpy as np

class Connect4Board(object):
    def __init__(self,  board_shape=(6, 7)):
        self.grid = np.zeros(board_shape, dtype=np.int8)
        self.height = np.zeros(board_shape[1], dtype=np.int8)
        self.player = 1
    def move(self, slot):# Add a piece to the board
        self.grid[self.height[slot], slot] = self.player
        self.height[slot] += 1
        # Update next player:
        if self.player < 0:# == -1
            self.player = 1
        else:# self.player == 1
            self.player = -1
        return
    def check(self):# Check if anyone has won
        pass
    def __str__(self):# String for print
        return str(self.grid[::-1])

class BoardExplorer(Connect4Board):
    def __init__(self,  board_shape=(6, 7), toWin=4):
        super().__init__(board_shape)
        self.toWin = toWin
        self.wins = []
    def findHorizWins(self):
        for i in range(self.grid.shape[1]-self.toWin+1):
            horiz = np.zeros(self.grid.shape[1], dtype=np.int8)
            for k in range(self.toWin):
                horiz[i+k] = 1
            for j in range(self.grid.shape[0]):
                self.grid[j] = horiz
                self.wins.append(np.where(self.grid > 0))
                print(super().__str__())
                super().__init__(self.grid.shape) #reset grid
        print("winpatterns:", len(self.wins))
    def findVerticalWns(self):
        for i in range(self.grid.shape[0]-self.toWin+1):
            vert = np.zeros((self.grid.shape[0], 1), dtype=np.int8)
            for k in range(self.toWin):
                vert[i+k][0] = 1
            for j in range(self.grid.shape[1]):
                self.grid[:,j] = vert[:,0]
                self.wins.append(np.where(self.grid > 0))
                print(super().__str__())
                super().__init__(self.grid.shape) #reset grid
        print("winpatterns:", len(self.wins))
    def findDiagWins(self):
        # first half:
        row = 0
        while(row < self.grid.shape[0]):
            col = 0
            rowTmp = row
            diag = []
            while rowTmp >= 0: # get the diagonal
                diag.append((rowTmp, col))
                rowTmp -= 1
                col += 1
            row += 1
            if len(diag) >= self.toWin:# if diag large enough,
                # step through all positions of a winning sequence on the grid:
                for i in range(len(diag)-self.toWin+1):
                    # Choose points:
                    winDiag = [diag[i+k] for k in range(self.toWin)]
                    # convert points to np.array indices
                    winIdx = (np.array([i for i, j in winDiag]), np.array([j for i, j in winDiag]))
                    self.grid[winIdx] = 1# winning diag = to 1
                    self.wins.append(np.where(self.grid > 0))#save points
                    print(super().__str__())
                    self.grid = np.flip(self.grid, axis=0)# flip vertically
                    self.wins.append(np.where(self.grid > 0))#save points
                    print(super().__str__())
                    self.grid = np.flip(self.grid, axis=1)# flip horizontally
                    self.wins.append(np.where(self.grid > 0))#save points
                    print(super().__str__())
                    self.grid = np.flip(self.grid, axis=0)# flip vertically
                    self.wins.append(np.where(self.grid > 0))#save points
                    print(super().__str__())
                    super().__init__(self.grid.shape)# reset grid
        print("winpatterns:", len(self.wins))
    def getWinPatterns(self):
        return np.array(self.wins)

if __name__ == "__main__":
    board = Connect4Board()
    board.move(1)
    board.move(1)
    print(board)

    explore = BoardExplorer()
    explore.findHorizWins()
    explore.findVerticalWns()
    explore.findDiagWins()
    wins = explore.getWinPatterns()
    print(wins.shape)
    print(type(wins[0]))
    print(board[wins[:,:,0]])
    # import timeit
    # print(timeit.timeit("[board[idcs] for idcs in wins]", setup="from __main__ import board, wins, np"))
