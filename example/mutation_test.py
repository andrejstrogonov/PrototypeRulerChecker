from pathlib import Path

from example.a import add_five
from example.b import is_match

src_loc = Path("example")


def open_print(fn):
    """Open a print file contents."""
    with open(fn) as f:
        print(f.read())


def test_add_five():
    assert add_five(6) > 10


def test_is_match():
    assert is_match("one", "one")


open_print(src_loc / "mutation_test.py")
