import pytest
from src.huffman_coding import encode

@pytest.mark.parametrize(
    ['input', 'expected'],
    [
        ("aaaaabbbbcccddffeeee", (51, 6)),
        ("abracadabra", (23,5)),
        ("abcdef", (16, 6)),
    ]
)
def test_basic_encode(input, expected):
    output = encode(input)
    assert (len(output[0]), len(output[1])) == expected

@pytest.mark.parametrize(
    ['input', 'expected'],
    [
        ("a", (1, 1)),
        ("", (0,0)),
        ("abababab", (8, 2)),
        ("a\nb\ta", (10, 4))
    ]
)
def test_edge_cases_encode(input, expected):
    output = encode(input)
    assert (len(output[0]), len(output[1])) == expected
