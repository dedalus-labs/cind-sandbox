"""Core math utilities."""

from __future__ import annotations


def fibonacci(n: int) -> int:
    """Return the *n*-th Fibonacci number (0-indexed).

    >>> fibonacci(0)
    0
    >>> fibonacci(6)
    8
    """
    if n < 0:
        msg = "n must be non-negative"
        raise ValueError(msg)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def clamp(value: float, low: float, high: float) -> float:
    """Clamp *value* to the inclusive range [*low*, *high*].

    >>> clamp(5, 0, 10)
    5
    >>> clamp(-3, 0, 10)
    0
    >>> clamp(15, 0, 10)
    10
    """
    if low > high:
        msg = f"low ({low}) must be <= high ({high})"
        raise ValueError(msg)
    return max(low, min(value, high))


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into a single sorted list.

    Both *a* and *b* must already be sorted in ascending order.

    >>> merge_sorted([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    result: list[int] = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    # BUG: the remaining elements of whichever list isn't exhausted
    # are never appended.  The correct fix is:
    #   result.extend(a[i:])
    #   result.extend(b[j:])
    return result
