# Multiplicação com Karatsuba

Este repositório implementa o **algoritmo de Karatsuba** para multiplicação eficiente de números inteiros grandes.  

## 🔢 O algoritmo de Karatsuba

A multiplicação tradicional entre números inteiros é feita em tempo O(n^2), onde n é o número de dígitos. O algoritmo de **Karatsuba** reduz essa complexidade para aproximadamente O(n^{log_2 3}) ≈ O(n^{1.585}), tornando a multiplicação entre grandes números bem mais rápida.

A ideia principal é **dividir para conquistar**:

Dado dois números u e v, com n dígitos:
1. Divide cada número em duas partes:
   - u = p * 10^m + q
   - v = r * 10^m + s
   onde m = floor(n/2).
2. Calcula três produtos menores:
   - A = p * r
   - B = q * s
   - C = (p+q)(r+s) - A - B
3. Combina os resultados:

    u * v = A * 10^(2m) + C * 10^m + B

Dessa forma, em vez de 4 multiplicações grandes, fazemos apenas **3**, o que reduz bastante o custo quando os números são grandes.

---

## 🚀 Como executar o script

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/karatsuba-python.git
cd karatsuba-python
```

### 2. Executar com Python
Este script não requer bibliotecas externas. Basta rodar:

```bash
python3 script.py <numero1> <numero2>
```

### 📌 Exemplo
```bash
python3 script.py 12345 6789
```

Saída esperada:
```
12345 * 6789 = 83810205
```





