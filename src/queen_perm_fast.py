def read_n():
    try:
        n = int(input("Enter N: "))
        if n <= 0:
            raise Exception("Expected N > 0")
    except ValueError:
        print("Expected a number!")
        return 0
    except Exception as err:
        print(err)
        return 0
    return n


def count_good_perms(n):
    def _count_good_perms(cols, left_diag, right_diag, ones):
        if cols == ones:
            return 1

        free_positions = ones & ~(left_diag | right_diag | cols)
        res = 0
        while free_positions:
            pos = free_positions & -free_positions
            free_positions &= ~pos

            res += _count_good_perms(
                cols | pos, (left_diag | pos) << 1, (right_diag | pos) >> 1, ones
            )

        return res

    ones = (1 << n) - 1
    return _count_good_perms(0, 0, 0, ones)


N = read_n()
if N <= 0:
    exit(1)

res = count_good_perms(N)

print(f"Good permutations: {res}")
