"""

Board is an array of queen position in the row in the 'i' column.

It is more effecient, because
you can place only one queen in one row and in one column,
so all we need is to check beating queens diagonally.

So all the queen permutations can be represented as
a permutations of an array of [1:n] numbers.

"""

def read_N():
    N = int(input("Enter N: "))
    if N <= 0:
        raise Exception("Expected N > 0")
    return N


def is_good_pos(board, col, row):
    for i in range(col):
        # Check if there are any  any queens on the same row
        # or any queens that beat our position diagonally.
        if row == board[i] or col - i == abs(row - board[i]):
            return False
    return True

def _count_good_perms_impl(board, col):
    # We have reached the end of the array
    # so we have made a good permutation.
    if len(board) <= col:
        return 1
    
    res = 0
    # Try to place a queen on 'col' column.
    for row in range(len(board)):
        # Check if we can use 'row' row.
        if is_good_pos(board, col, row):
            board[col] = row
            res += _count_good_perms_impl(board, col + 1)

    return res

def count_good_perms(N):
    board = [-1] * N
    return _count_good_perms_impl(board, 0)


try:
    N = read_N()
    res = count_good_perms(N)
    print(f"Good permutations: {res}")
except ValueError:
    print("Expected a number!")
except Exception as err:
    print(err)