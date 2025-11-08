import pytest
import src.huffman_coding


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ("aaaaabbbbcccddffeeee", (51, 6)),
        ("abracadabra", (23, 5)),
        ("abcdef", (16, 6)),
    ],
)
def test_basic_encode(input, expected):
    output = src.huffman_coding.encode(input)
    assert (len(output[0]), len(output[1])) == expected


@pytest.mark.parametrize(
    ["input", "expected"],
    [("a", (1, 1)), ("", (0, 0)), ("abababab", (8, 2)), ("a\nb\ta", (10, 4))],
)
def test_edge_cases_encode(input, expected):
    encoded, codes = src.huffman_coding.encode(input)
    assert (len(encoded), len(codes)) == expected


@pytest.mark.parametrize(
    ["codes", "encoded", "decoded"],
    [
        (
            {
                " ": "000",
                "d": "001",
                "h": "010",
                "w": "011",
                "l": "10",
                "o": "110",
                "r": "1110",
                "e": "1111",
            },
            "01011111010110000011110111010001",
            "hello world",
        ),
        ({"a": "0", "b": "1"}, "010101", "ababab"),
        ({"a": "0", "b": "10", "c": "110", "d": "111"}, "01011010111", "abcbd"),
        (
            {"c": "00", "b": "01", "e": "10", "a": "110", "d": "111"},
            "110101110100",
            "aedbc",
        ),
        (
            {"a": "0", "c": "100", "d": "101", "r": "110", "b": "111"},
            "01111100100010101111100",
            "abracadabra",
        ),
    ],
)
def test_basic_decode(codes, encoded, decoded):
    assert src.huffman_coding.decode(codes, encoded) == decoded


@pytest.mark.parametrize(
    ["codes", "encoded", "decoded"],
    [
        ({"a": "0"}, "00000", "aaaaa"),
        ({}, "", ""),
        ({"a": "0"}, "0", "a"),
    ],
)
def test_edge_cases_decode(codes, encoded, decoded):
    assert src.huffman_coding.decode(codes, encoded) == decoded


@pytest.mark.parametrize(
    "input",
    [
        " ",
        "abc abc",
        "Hello, world!",
        "a",
    ],
)
def test_encode_decode(input):
    encoded, codes = src.huffman_coding.encode(input)
    assert src.huffman_coding.decode(codes, encoded) == input
