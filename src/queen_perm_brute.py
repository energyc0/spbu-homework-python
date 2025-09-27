import itertools

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

def is_good_perm(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if j - i == abs(board[j] - board[i]):
                return False
    return True

def count_good_perms(N):
    res = 0

    for perm in itertools.permutations(range(N)):
        if is_good_perm(perm):
            res += 1

    return res

N = read_N()
if N <= 0:
    exit(1)
    
res = count_good_perms(N)

print(f"Good permutations: {res}")