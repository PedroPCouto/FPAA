📘 Multiplicação de Inteiros com o Algoritmo de Karatsuba

## 🔍 O que é o algoritmo de Karatsuba?

O algoritmo de **Karatsuba** é uma técnica de multiplicação rápida para números inteiros grandes, desenvolvida por Anatolii Karatsuba em 1960.  

A multiplicação tradicional de dois números com \\( n \\) dígitos tem complexidade \\( O(n^2) \\). Karatsuba conseguiu reduzir isso para aproximadamente \\( O(n^{\\\\log_2 3}) \\), ou seja, cerca de \\( O(n^{1.585}) \\).  

A ideia principal é **dividir os números em metades** e evitar multiplicações desnecessárias através de um truque algébrico.  

Se temos dois números:  

\\[
u = p \\\\cdot 10^m + q \\\\quad \\\\quad v = r \\\\cdot 10^m + s
\\]

Karatsuba observa que:  

\\[
u \\\\cdot v = p \\\\cdot r \\\\cdot 10^{2m} + (p \\\\cdot s + q \\\\cdot r) \\\\cdot 10^m + q \\\\cdot s
\\]

Isso permite calcular o produto usando apenas **3 multiplicações diretas** ao invés de 4, reduzindo o custo computacional.

---

## 🖥️ Estrutura do Script

O script implementa a multiplicação de dois inteiros utilizando Karatsuba. Ele recebe **dois números inteiros como argumentos via terminal**, multiplica-os e imprime o resultado.

```python
def karatsuba(u, v):
    n = max(len(str(u)), len(str(v)))
    if n == 1:
        return u * v
    half = n // 2
    p, q = divmod(u, 10**half)
    r, s = divmod(v, 10**half)

    return p * r * 10**n + (p * s + q * r) * 10**half + q * s
