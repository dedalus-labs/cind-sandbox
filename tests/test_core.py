"""Tests for mathutils.core."""

from __future__ import annotations

import pytest

from mathutils.core import clamp, fibonacci, merge_sorted


# --- fibonacci ---


def test_fibonacci_base_cases() -> None:
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_fibonacci_sequence() -> None:
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55


def test_fibonacci_negative_raises() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-1)


# --- clamp ---


def test_clamp_within_range() -> None:
    assert clamp(5, 0, 10) == 5


def test_clamp_below() -> None:
    assert clamp(-3, 0, 10) == 0


def test_clamp_above() -> None:
    assert clamp(15, 0, 10) == 10


def test_clamp_boundaries() -> None:
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_clamp_invalid_range() -> None:
    with pytest.raises(ValueError, match="low"):
        clamp(5, 10, 0)


# --- merge_sorted ---


def test_merge_sorted_equal_length() -> None:
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_unequal_length() -> None:
    assert merge_sorted([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_merge_sorted_empty_left() -> None:
    assert merge_sorted([], [1, 2, 3]) == [1, 2, 3]


def test_merge_sorted_empty_right() -> None:
    assert merge_sorted([1, 2, 3], []) == [1, 2, 3]


def test_merge_sorted_both_empty() -> None:
    assert merge_sorted([], []) == []
