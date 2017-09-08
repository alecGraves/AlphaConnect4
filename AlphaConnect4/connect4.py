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
        summ = 0
        for i in wins:
            summ = board.grid[i][0] + board.grid[i][1] + board.grid[i][2] + board.grid[i][3]
            if summ == 4 or sum == -4:
                return summ/4
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
                self.wins.append(self.grid)
                # self.wins.append(np.where(self.grid > 0))
                print(super().__str__())
                super().__init__(self.grid.shape) #reset grid
        # print("winpatterns:", len(self.wins))
    def findVerticalWns(self):
        for i in range(self.grid.shape[0]-self.toWin+1):
            vert = np.zeros((self.grid.shape[0], 1), dtype=np.int8)
            for k in range(self.toWin):
                vert[i+k][0] = 1
            for j in range(self.grid.shape[1]):
                self.grid[:,j] = vert[:,0]
                self.wins.append(self.grid)
                # self.wins.append(np.where(self.grid > 0))
                print(super().__str__())
                super().__init__(self.grid.shape) #reset grid
        # print("winpatterns:", len(self.wins))
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
                    self.wins.append(self.grid)
                    # self.wins.append(np.where(self.grid > 0))#save points
                    print(super().__str__())
                    self.grid = np.flip(self.grid, axis=0)# flip vertically
                    self.wins.append(self.grid)
                    # self.wins.append(np.where(self.grid > 0))#save points
                    print(super().__str__())
                    self.grid = np.flip(self.grid, axis=1)# flip horizontally
                    self.wins.append(self.grid)
                    # self.wins.append(np.where(self.grid > 0))#save points
                    print(super().__str__())
                    self.grid = np.flip(self.grid, axis=0)# flip vertically
                    self.wins.append(self.grid)
                    # self.wins.append(np.where(self.grid > 0))#save points
                    print(super().__str__())
                    super().__init__(self.grid.shape)# reset grid
        print("winpatterns:", len(self.wins))
    def getWinPatterns(self):
        self.findHorizWins()
        self.findVerticalWns()
        self.findDiagWins()
        return self.wins

if __name__ == "__main__":
    board = Connect4Board()
    board.move(1)
    board.move(1)
    print(board)

    explore = BoardExplorer()
    explore.findHorizWins()
    explore.findVerticalWns()
    explore.findDiagWins()
    winFilters = explore.getWinPatterns()
    print(wins[0][1])

    # print("wins = [")
    # for i in wins:
    #     print("(np.array([{},{},{},{}], dtype=np.int32), np.array([{},{},{},{}], dtype=np.int32)),".format(
    #     i[0][0], i[0][1], i[0][2], i[0][3], i[1][0], i[1][1], i[1][2], i[1][3]))
    # print("]")
    # exit()



    import timeit
    x = np.ndarray((6, 7), dtype=np.int8)
    y = np.ndarray((6, 7, 69), dtype=np.int8)
    print(timeit.timeit("np.sum(np.dot(x, y))", setup="from __main__ import x, y, np", number=10000)/10000)
    print(timeit.timeit("np.sum(np.array([board.grid[i] for i in wins]), axis=1)", setup="from __main__ import board, wins, np", number=1000)/1000)
    print(timeit.timeit("board.check()", setup="from __main__ import board", number=1000)/1000)


    # print(timeit.timeit("board = Connect4Board()", setup="from __main__ import Connect4Board", number=1000)/1000)
    # import time
    # N = 1000
    # start = time.time()
    # for i in range(N):
    #     board = Connect4Board()
    #     for k in range(6):
    #         for j in range(7):
    #             board.move(j)
    #             [np.sum(board.grid[i]) for i in wins]
    #
    # print(1000/(time.time()-start))
