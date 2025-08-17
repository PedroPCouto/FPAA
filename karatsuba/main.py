#Seja 'p' o número formado pelos n/2 primeiros dígitos de u 
#E seja 'q' o número formado pelos n/2 últimos dígitos de u

#Seja 'r' o número formado pelos n/2 primeiros dígitos de v
#E seja 's' o número formado pelos n/2 últimos dígitos de v

# Karatsuba: u × v  =  p × r × 10^n + (p × s + q × r) × 10^n/2 + q × s
import sys

def karatsuba(u, v):
    n = max(len(str(u)), len(str(v)))
    if n == 1:
        return u * v
    half = n // 2
    p, q = divmod(u, 10**half)
    r, s = divmod(v, 10**half)

    return p * r * 10**n + (p * s + q * r) * 10**half + q * s
    # Ou alternativamente: 
    # karatsuba(p * r) * 10**n + (karatsuba(p, s) + karatsuba(q, r)) * 10**half + karatsuba(q, s), 
    # mas isso custa bem mais memória e tempo


def main(u, v):
    result = karatsuba(u, v)
    print(f"{u} * {v} = {result}")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

