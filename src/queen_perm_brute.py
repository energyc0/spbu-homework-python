import itertools

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

def is_good_perm(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if there is a 'j' queen that beats our 'i' queen diagonally.
            if j - i == abs(board[j] - board[i]):
                return False
    return True

def count_good_perms(N):
    res = 0
    # Generate board permutation for is_good_perm() function.
    for perm in itertools.permutations(range(N)):
        if is_good_perm(perm):
            res += 1

    return res

try:
    N = read_N()
    res = count_good_perms(N)
    print(f"Good permutations: {res}")
except ValueError:
    print("Expected a number!")
except Exception as err:
    print(err)
