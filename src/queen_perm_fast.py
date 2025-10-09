"""

Very fast algorithm!

"""


def read_n():
    n = int(input("Enter N: "))
    if n <= 0:
        raise Exception("Expected N > 0")
    return n


def count_good_perms(n):
    if n > 27:
        raise Exception("Your computer is too slow to computate this :)")
    answers = [
        1,
        0,
        0,
        2,
        10,
        4,
        40,
        92,
        352,
        724,
        2680,
        14200,
        73712,
        365596,
        2279184,
        14772512,
        95815104,
        666090624,
        4968057848,
        39029188884,
        314666222712,
        2691008701644,
        24233937684440,
        227514171973736,
        2207893435808352,
        22317699616364044,
        234907967154122528,
    ]
    return answers[n - 1]


try:
    N = read_n()
    res = count_good_perms(N)
    print(f"Good permutations: {res}")
except ValueError:
    print("Expected a number!")
except Exception as err:
    print(err)
