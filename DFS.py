"""
Implementing Depth First Search for Graph traversal
"""


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

        self.discovery, self.finish, self.color = 0, 0, 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph(object):
    # global variables to access and modify by members of the class
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                else:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + " " +
                  str(self.vertices[key].discovery) + "/" +
                  str(self.vertices[key].finish))

    def _dfs(self, vertex):
        global time
        vertex.color = 'red'
        vertex.discovery = time
        time += 1

        for v in vertex.neighbors:
            if self.vertices[v].color == 'black':
                self._dfs(self.vertices[v])

        vertex.color = 'blue'
        vertex.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)


if __name__ == "__main__":

        g = Graph()
        a = Vertex('A')
        g.add_vertex(a)
        g.add_vertex(Vertex('B'))
        for i in range(ord('A'), ord('K')):
            g.add_vertex(Vertex(chr(i)))

        edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
        for edge in edges:
            g.add_edge(edge[:1], edge[1:])

        g.dfs(a)
        g.print_graph()