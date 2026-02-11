# cind-sandbox

A tiny Python project with a **deliberate bug** for end-to-end testing of
[cind](https://github.com/dedalus-labs/dedalus/tree/dev/tools/cind).

## The bug

`mathutils.core.merge_sorted` drops trailing elements when one input list is
longer than the other.  The test suite catches this:

```
FAILED tests/test_core.py::test_merge_sorted_unequal_length
FAILED tests/test_core.py::test_merge_sorted_empty_left
FAILED tests/test_core.py::test_merge_sorted_empty_right
```

## Usage

```bash
pip install pytest
pytest
```

## Purpose

This repo exists so `@cind fix` can be tested safely without touching
production code.  File an issue describing the bug, comment `@cind fix`, and
verify the full plan → approve → apply → PR loop.
