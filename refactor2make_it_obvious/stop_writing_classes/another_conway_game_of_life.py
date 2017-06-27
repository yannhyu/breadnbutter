# another_conway_game_of_life.py

def neighbors(cell):
    x, y = cell
    yield x - 1, y - 1
    yield x    , y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x    , y + 1
    yield x + 1, y + 1

def apply_iteration(board):
    new_board = set([])
    candidates = board.union(set(n for cell in board for n in neighbors(cell)))
    for cell in candidates:
        count = sum((n in board) for n in neighbors(cell))
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    return new_board

if __name__ == "__main__":
    board = {(0,1), (1,2), (2,0), (2,1), (2,2)}
    number_of_iterations = 10
    for _ in range(number_of_iterations):
        board = apply_iteration(board)
    print(board)