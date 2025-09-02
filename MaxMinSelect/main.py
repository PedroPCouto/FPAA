from typing import Iterable, Tuple, List

def maxmin_select(arr: List[float]) -> Tuple[float, float]:
    n = len(arr)
    if n == 0:
        raise ValueError("A lista não pode ser vazia.")

    return _maxmin_rec(arr, 0, n - 1)


def _maxmin_rec(arr: List[float], left: int, right: int) -> Tuple[float, float]:
    if left == right:
        x = arr[left]
        return x, x

    if right == left + 1:
        a, b = arr[left], arr[right]
        if a < b:
            return a, b
        else:
            return b, a

    mid = (left + right) // 2
    min_left, max_left = _maxmin_rec(arr, left, mid)
    min_right, max_right = _maxmin_rec(arr, mid + 1, right)

    overall_min = min_left if min_left < min_right else min_right
    overall_max = max_left if max_left > max_right else max_right

    return overall_min, overall_max


if __name__ == "__main__":
    exemplos = [
        [3, 1, 7, 2, 9, 5],
        [10],
        [2, 2, 2, 2],
        [-5, 0, 12, -3, 4],
        [9, -1]
    ]

    for i, arr in enumerate(exemplos, 1):
        mn, mx = maxmin_select(arr)
        print(f"Exemplo {i}: arr={arr} -> min={mn}, max={mx}")
