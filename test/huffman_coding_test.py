import pytest
import src.huffman_coding

@pytest.mark.parametrize(
    ['input', 'expected'],
    [
        ('aaaaabbbbcccddffeeee', (51, 6)),
        ('abracadabra', (23,5)),
        ('abcdef', (16, 6)),
    ]
)
def test_basic_encode(input, expected):
    output = src.huffman_coding.encode(input)
    assert (len(output[0]), len(output[1])) == expected

@pytest.mark.parametrize(
    ['input', 'expected'],
    [
        ('a', (1, 1)),
        ('', (0,0)),
        ('abababab', (8, 2)),
        ('a\nb\ta', (10, 4))
    ]
)
def test_edge_cases_encode(input, expected):
    output = src.huffman_coding.encode(input)
    assert (len(output[0]), len(output[1])) == expected

@pytest.mark.parametrize(
    ['codes', 'encoded', 'decoded'],
    [
        ({' ': '000', 'd': '001', 'e': '010', 'h': '011', 'r': '100',
             'w': '101', 'l': '11', 'o': '10'},
             '01101011111010000101111010001001', 'hello world'),
        ({'a':0, 'b':1} ,
          '010101', 'abababab'),
        ({'a': '0', 'b': '10', 'c': '110', 'd': '111'},
           '010110110111', 'abcbd'),
        ({'a': '00', 'b': '01', 'c': '10', 'd': '110', 'e': '111'},
          '0001110100110', 'aedbc'),
        ({'a': '0', 'b': '100', 'r': '101', 'c': '1100', 'd': '1101'},
          '010010101100011010100', 'abracadabra')
    ]
)
def test_basic_decode(codes, encoded, decoded):
    assert src.huffman_coding.decode(codes, encoded) == decoded

@pytest.mark.parametrize(
    ['codes', 'encoded', 'decoded'],
    [
        ({'a': '0'}, '00000', 'aaaaa'),
        ({},'', ''),
        ({'a': '0'}, '0', 'a'),
    ]
)
def test_edge_cases_decode(codes, encoded, decoded):
    assert src.huffman_coding.decode(codes, encoded) == decoded
