# MaxMin Select (Divisão e Conquista) em Python

Implementação do algoritmo de seleção simultânea do menor e do maior elemento (MaxMin Select) usando a estratégia de divisão e conquista (recursiva).

## Como executar

Pré-requisitos:
- Python 3.8+ instalado

Passos:
1. Clone ou baixe este repositório.
2. No terminal, dentro da pasta do projeto, execute:
   ```bash
   python3 main.py
   ```
3. Você verá a saída com os exemplos de teste do `__main__`.

Para usar a função no seu próprio código:
```python
from main import maxmin_select

arr = [3, 1, 7, 2, 9, 5]
mn, mx = maxmin_select(arr)
print(mn, mx)
```

## Explicação do algoritmo (linha a linha)

Arquivo: `main.py`

- `maxmin_select(arr)`: função de alto nível.
  - Valida que a lista não é vazia.
  - Chama `_maxmin_rec(arr, 0, n-1)` para resolver o problema no intervalo todo.

- `_maxmin_rec(arr, left, right)`:
  - Caso base (1 elemento): quando `left == right`, retorna `(x, x)`.
  - Caso base (2 elementos): quando `right == left + 1`, faz 1 comparação entre `a` e `b` e retorna `(min, max)`.
  - Passo recursivo:
    - Divide o problema ao meio: `mid = (left + right) // 2`.
    - Resolve recursivamente os subproblemas `[left, mid]` e `[mid+1, right]`.
    - Combina os resultados com apenas 2 comparações:
      - `overall_min = min(min_left, min_right)`
      - `overall_max = max(max_left, max_right)`

A estratégia reduz comparações: em vez de comparar cada elemento duas vezes (abordagem ingênua), comparamos pares de subproblemas e agregamos com 2 comparações por nível.

## Relatório técnico

### 1) Análise por contagem de operações (comparações)

Definição: seja `C(n)` o número de comparações entre elementos do arr para computar simultaneamente min e max em um array de tamanho `n`.

- Casos base:
  - `n = 1`: `C(1) = 0` (não há comparação).
  - `n = 2`: `C(2) = 1` (uma comparação entre os dois elementos).

- Passo recursivo (para `n >= 3`):
  - Dividimos o array em duas metades, de tamanhos aproximadamente `n/2` e `n/2`.
  - Resolvemos recursivamente: custo `C(⌊n/2⌋) + C(⌈n/2⌉)`.
  - Combinação: 2 comparações (uma para decidir o menor entre os dois mínimos, outra para o maior entre os dois máximos).

Para simplificação assintótica, considerando `n` potência de 2:
- Recorrência: `C(n) = 2·C(n/2) + 2`, com `C(1) = 0`.

Resolvendo por expansão:
- Nível 0: `+2`
- Nível 1: `2 * (+2) = +4`
- Nível 2: `4 * (+2) = +8`
- ...
- Nível k (onde `n = 2^k`): `2^k * 2 = 2n`

Somando os níveis de `0` a `log2 n - 1`:
- Soma geométrica: `2 * (2^{log2 n} - 1) = 2 * (n - 1) = 2n - 2`.

Logo, `C(n) = 2n - 2` para `n` potência de 2. Para `n` gerais, a expressão é `C(n) = 2n - Θ(1)`, isto é, linear no tamanho da entrada.

Conclusão: complexidade temporal é `O(n)` e número de comparações é aproximadamente `2n - 2`.

Observação: Outras variações do algoritmo de MaxMin (como comparar elementos em pares antes de comparar a min/max) alcançam `⌊3n/2⌋ - 2` comparações. Nosso esquema de divisão e conquista com 2 comparações por combinação apresenta `2n - 2` comparações assintoticamente (ainda O(n)).

### 2) Teorema Mestre

Recorrência de tempo (custos dominantes em função de n, desprezando casos base):
- `T(n) = 2 T(n/2) + O(1)`.

Na forma padrão:
- `a = 2`
- `b = 2`
- `f(n) = O(1)`

Cálculo de `p = log_b a = log_2 2 = 1`.

Comparação de `f(n)` com `n^p = n^1 = n`:
- `f(n) = O(1) = O(n^{p - ε})` com `ε = 1`.

Portanto, caso 1 do Teorema Mestre:
- `T(n) = Θ(n^p) = Θ(n)`.

Conclusão: a complexidade temporal é linear, `Θ(n)`.
