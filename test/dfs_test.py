import pytest
from src.dfs import Graph


@pytest.mark.parametrize(
    ["edges", "dfs_traverse"],
    [
        ([[1, 2], [0, 2], [0, 1]], [0, 2, 1]),  # triangle
        ([[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]], [0, 2, 3, 1]),  # rhomb
        (
            [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0]],
            [0, 5, 4, 3, 2, 1],
        ),  # cyclic
        (
            [[1, 2], [0, 3, 4], [0, 5, 6], [1, 7], [1, 6], [2, 7], [2, 4], [5, 3]],
            [0, 2, 6, 4, 1, 3, 7, 5],
        ),  # complex
    ],
)
def test_graphs(edges, dfs_traverse):
    gr = Graph(edges)
    for i in range(len(edges)):
        for j in range(len(edges)):
            assert gr.has_path(i, j)
    assert gr.dfs() == dfs_traverse
    assert list(gr) == dfs_traverse

    it = iter(gr)
    for i in range(len(edges)):
        next(it)

    with pytest.raises(StopIteration):
        next(it)

    with pytest.raises(StopIteration):
        next(it)
