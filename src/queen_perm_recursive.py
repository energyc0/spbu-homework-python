def read_N():
    try:
        N = int(input("Enter N: "))
        if N <= 0:
            raise Exception("Expected N > 0")
    except ValueError:
        print("Expected a number!")
        return 0
    except Exception as err:
        print(err)
        return 0
    return N

def is_good_pos(board, col, row):
    for i in range(col):
        if row == board[i] or col - i == abs(row - board[i]):
            return False
    return True

def _count_good_perms_impl(board, col):
    if len(board) <= col:
        return 1
    
    res = 0
    for row in range(len(board)):
        if is_good_pos(board, col, row):
            board[col] = row
            res += _count_good_perms_impl(board, col + 1)

    return res

def count_good_perms(N):
    board = [-1] * N
    return _count_good_perms_impl(board, 0)


N = read_N()
if N <= 0:
    exit(1)

res = count_good_perms(N)

print(f"Good permutations: {res}")