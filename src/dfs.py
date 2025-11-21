class Graph:
    def __init__(self, vertices: list[list[int]]) -> None:
        '''
        First index of vertices is the index of vertex,
        the list of vertices[index] is neighbours of vertex.
        '''
        self.vertices = vertices

    def has_path(self, a_vertex: int, b_vertex: int) -> bool:
        '''
        Find whether a_vertex is connected with b_vertex.
        a_vertex and b_vertex is index of vertices.
        '''
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
        '''
        Depth-first search algorithm.
        Returns all the vertices in the order of the algorithm's passage.
        '''
        visited = []
        to_visit = list(range(len(self.vertices)-1, -1, -1))

        while len(to_visit) > 0:
            vertex = to_visit.pop()
            if vertex in visited:
                continue
            visited.append(vertex)
            for v in self.vertices[vertex]:
                to_visit.append(v)

        return visited
            

edges = [
    [1, 2],       # Компонента 1: 0-1-2
    [0],
    [0],
    [4, 5],       # Компонента 2: 3-4-5
    [3],
    [3],
    []            # Изолированная вершина
]
# Пути: 0→2: [0,2], 3→5: [3,5], 0→6: нет пути
gr = Graph(edges)
print(gr.has_path(0, 3))
print(gr.dfs())
l = list(range(5, 0, -1))
print(l)