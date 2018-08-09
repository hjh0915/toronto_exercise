HIT = 'X'
MISS = 'M'

def count_hits_and_misses(board):
    """ (list of list of str) -> list of int

    Precondition: board != [] and each list in board has len(board)

    Return a list that contains the number of occurrences of the
    HIT or MISS symbol in each row of board.

    >>> board = [['-','M','-'], ['X','M','-'], ['-','-','-']]
    >>> count_hits_and_misses(board)
    [1, 2, 0]
    """
    
    s = []
    #遍历
    for i in board:
        #累加
        num = 0
        for j in i:
            if j == HIT or j == MISS:
                num = num + 1
        s.append(num)
    return s 

if __name__ == '__main__':
    board = [['-','M','-'], ['X','M','-'], ['-','-','-']]
    print(count_hits_and_misses(board))