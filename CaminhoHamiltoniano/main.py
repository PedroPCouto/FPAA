from typing import Dict, List, Optional, Set, Tuple

class Graph:
    def __init__(self, is_directed: bool = False):
        self.adj: Dict[str, List[str]] = {}
        self.is_directed = is_directed

    def add_vertex(self, v: str):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u: str, v: str):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        if not self.is_directed:
            self.adj[v].append(u)

    @classmethod
    def from_edges(cls, edges: List[Tuple[str, str]], is_directed: bool = False):
        g = cls(is_directed=is_directed)
        for u, v in edges:
            g.add_edge(u, v)
        return g

def hamiltonian_path_backtracking(graph: Graph) -> Optional[List[str]]:
    vertices = list(graph.adj.keys())
    n = len(vertices)
    if n == 0:
        return []

    def backtrack(path: List[str], visited: Set[str]) -> Optional[List[str]]:
        if len(path) == n:
            return path[:]  
        last = path[-1]
        for nei in graph.adj.get(last, []):
            if nei not in visited:
                visited.add(nei)
                path.append(nei)
                res = backtrack(path, visited)
                if res is not None:
                    return res
                path.pop()
                visited.remove(nei)
        return None

    for start in vertices:
        visited = {start}
        path = [start]
        res = backtrack(path, visited)
        if res is not None:
            return res
    return None

def has_hamiltonian_path(graph: Graph) -> bool:
    return hamiltonian_path_backtracking(graph) is not None

def example_graph_undirected() -> Graph:
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("B", "D"),
        ("A", "C"),
    ]
    return Graph.from_edges(edges, is_directed=False)

def example_graph_directed() -> Graph:
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("A", "C"),
        ("B", "D"),
    ]
    return Graph.from_edges(edges, is_directed=True)

if __name__ == "__main__":
    g_und = example_graph_undirected()
    path_und = hamiltonian_path_backtracking(g_und)
    print("Não dirigido:")
    if path_und:
        print("Caminho Hamiltoniano encontrado:", " -> ".join(path_und))
    else:
        print("Não existe caminho Hamiltoniano.")

    g_dir = example_graph_directed()
    path_dir = hamiltonian_path_backtracking(g_dir)
    print("\nDirigido:")
    if path_dir:
        print("Caminho Hamiltoniano encontrado:", " -> ".join(path_dir))
    else:
        print("Não existe caminho Hamiltoniano.")
