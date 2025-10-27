# Caminho Hamiltoniano em Python

Este projeto implementa um algoritmo de backtracking para encontrar um Caminho Hamiltoniano em grafos dirigidos e não dirigidos.

## Descrição do projeto

Um Caminho Hamiltoniano é um caminho que visita cada vértice do grafo exatamente uma vez. O problema de decidir se existe tal caminho é classicamente estudado em teoria dos grafos e complexidade.

Neste projeto, usamos backtracking: tentamos construir incrementalmente um caminho, adicionando vértices ainda não visitados que são adjacentes ao último do caminho. Quando travamos (não há expansão possível), retrocedemos (backtrack) e tentamos outra opção.

## Lógica do algoritmo (linha a linha)

Arquivo `main.py`:

- `class Graph`: estrutura de grafo com lista de adjacência; suporta `is_directed`.
  - `add_vertex`/`add_edge`: garantem registro de vértices e arestas (dupla inserção se não dirigido).
  - `from_edges`: atalho para construir a partir de uma lista de arestas.
- `hamiltonian_path_backtracking(graph)`:
  - Converte vértices para lista `vertices` e guarda `n`.
  - Se `n == 0`, retorna lista vazia (caso trivial).
  - Define função interna `backtrack(path, visited)`:
    - Se `len(path) == n`, visitamos todos os vértices: retornamos cópia do caminho.
    - Caso contrário, olhamos o último vértice `last` e tentamos cada vizinho `nei` não visitado:
      - Marcamos `nei` como visitado, anexamos ao caminho e chamamos recursivamente.
      - Se a chamada devolve um caminho, propagamos sucesso.
      - Caso contrário, desfazemos (pop e remove do `visited`) e testamos outro vizinho.
    - Se nenhum vizinho leva a solução, retorna `None`.
  - Loop externo: tenta cada vértice como início (`start`), inicia `visited` e `path`, e chama `backtrack`.
  - Retorna o primeiro caminho encontrado ou `None` se nenhum existir.
- `has_hamiltonian_path`: atalho booleano.
- `example_graph_undirected`/`example_graph_directed`: pequenos grafos de exemplo.
- Bloco `if __name__ == "__main__"`: executa testes simples e imprime o resultado.

Observação: A ordem dos vizinhos e dos vértices influencia qual caminho é encontrado primeiro, mas não a corretude.

## Como executar

Pré-requisitos:
- Python 3.9+.

Passos:
1. Clone o repositório.
2. Opcional: crie um virtualenv e ative.
3. Execute:
   ```bash
   python main.py
