class Graph:
    def __init__(self, vertices: list[list[int]]) -> None:
        """
        First index of vertices is the index of vertex,
        the list of vertices[index] is neighbours of vertex.
        """
        self.vertices = vertices

    def has_path(self, a_vertex: int, b_vertex: int) -> bool:
        """
        Find whether a_vertex is connected with b_vertex.
        a_vertex and b_vertex is index of vertices.
        """
        visited = []
        to_visit = [a_vertex]
        while len(to_visit) > 0:
            vertex = to_visit.pop()
            if vertex == b_vertex:
                return True
            if vertex in to_visit:
                continue
            visited.append(vertex)
            for v in self.vertices[vertex]:
                if v not in visited:
                    to_visit.append(v)

        return False

    def dfs(self) -> list[int]:
        """
        Depth-first search algorithm.
        Returns all the vertices in the order of the algorithm's passage.
        """
        return list(self)

    def __iter__(self):
        return GraphIterator(self)


class GraphIterator:
    """
    Traverse graph in order of depth-search algorithm.
    """

    def __init__(self, graph: Graph):
        self.vertices = graph.vertices.copy()
        self.to_visit = list(range(len(graph.vertices) - 1, -1, -1))
        self.visited = []

    def __next__(self) -> int:
        while len(self.to_visit) > 0:
            vertex = self.to_visit.pop()
            if vertex in self.visited:
                continue
            self.visited.append(vertex)
            for v in self.vertices[vertex]:
                self.to_visit.append(v)
            return vertex
        raise StopIteration
