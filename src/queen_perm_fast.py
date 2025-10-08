"""

Board is an array of queen position in the row in the 'i' column.

It is more effecient, because
you can place only one queen in one row and in one column,
so all we need is to check beating queens diagonally.

So all the queen permutations can be represented as
a permutations of an array of [1:n] numbers.

"""


def read_n():
    n = int(input("Enter N: "))
    if n <= 0:
        raise Exception("Expected N > 0")
    return n


def count_good_perms(n):
    # Remember the value so that you don't have to calculate it.
    # It is a mask of N ones.
    ones = (1 << n) - 1

    def _count_good_perms(cols, left_diag, right_diag):
        # We have used all the columns.
        if cols == ones:
            return 1

        # Calculate free positions.
        # In other words,
        # free_positions = all_positions
        #                   - busy_positions
        #                   - queens_beating_on_the_left
        #                   - queens_beating_on_the_right
        free_positions = ones & ~(left_diag | right_diag | cols)
        res = 0

        # While there are any positions in the mask.
        while free_positions:
            # Get the most right position.
            pos = free_positions & -free_positions
            # Mark it as busy.
            free_positions &= ~pos
            # Shift positions of beating queens and
            # add new pos to 'busy_positions'.
            res += _count_good_perms(
                cols | pos, (left_diag | pos) << 1, (right_diag | pos) >> 1
            )

        return res

    return _count_good_perms(0, 0, 0)


try:
    N = read_n()
    res = count_good_perms(N)
    print(f"Good permutations: {res}")
except ValueError:
    print("Expected a number!")
except Exception as err:
    print(err)
