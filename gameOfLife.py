from PIL import Image
def numLivingNeighbours(board, i, j, xDim, yDim):
    count = 0
    if i>0:
        if j > 0:
            count += board[i-1][j-1]
        count+=board[i-1][j]
        if j<xDim-1:
            count+=board[i-1][j+1]
    if j>0:
        count += board[i][j-1]
    if j<xDim-1:
        count+=board[i][j+1]

    if i<yDim-1:
        if j>0:
            count += board[i+1][j-1]
        count+=board[i+1][j]
        if j<xDim-1:
            count+=board[i+1][j+1]
    return count




def evaluate(board, visualise=False):
    if visualise:
        frames = []
    count = 0
    boardHistory = []
    boardHash = hash(str(board))
    xDim = len(board)
    yDim = len(board[0])

    while(sum(map(sum, board))>0 and boardHash not in boardHistory):
        if(visualise):
            im = Image.new('RGB',(len(board),len(board[0])))

            im.putdata(list(sum(map(lambda x: list(map(lambda y: (int(y)*255,int(y)*255,int(y)*255),x)),board),[])))
            frames.append(im)


        boardHistory.append(boardHash)
        if len(boardHistory)>150:
            boardHistory = boardHistory[:-100]
        newBoard = []
        for i, row in enumerate(board):
            newRow = []
            for j in range(len(row)):
                numLiving = numLivingNeighbours(board, i, j, xDim, yDim)
                if board[i][j]:
                    if numLiving<2:
                        newRow.append(False)
                    elif numLiving>3:
                        newRow.append(False)
                    else:
                        newRow.append(True)
                else:
                    if numLiving == 3:
                        newRow.append(True)
                    else:
                        newRow.append(False)
            newBoard.append(newRow)
        board = newBoard
        boardHash = hash(str(board))
        count+=1
    if visualise:
        return count, frames
    return count
