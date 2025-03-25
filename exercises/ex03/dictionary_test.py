"""Dictionary Functions Test."""

__author__ = "730515621"

from dictionary import invert
from dictionary import count
from dictionary import favorite_color
from dictionary import bin_len


def test_1_invert() -> None:
    """Test use case 1 for invert function."""
    assert invert({"cat": "dog"}) == {"dog": "cat"}


def test_2_invert() -> None:
    """Test use case 2 for invert fuction."""
    assert invert({"apple": "banana"}) == {"banana": "apple"}


def test_3_invert() -> None:
    """Test edge case for invert function."""
    assert invert({}) == {}


def test_1_count() -> None:
    """Test use case 1 for count function."""
    assert count(["blue", "blue", "blue", "red", "green"]) == {
        "blue": 3,
        "red": 1,
        "green": 1,
    }


def test_2_count() -> None:
    """Test use case 2 for count function."""
    assert count(["cat", "dog"]) == {"cat": 1, "dog": 1}


def test_3_count() -> None:
    """Test edge case 3 for count function."""
    assert count(["", ""]) == {"": 2}


def test_1_favorite_color() -> None:
    """Test use case 1 for favorite color function."""
    assert favorite_color({"Sally": "blue", "Joe": "red", "John": "red"}) == "red"


def test_2_favorite_color() -> None:
    """Test use case 2 for favorite color function."""
    assert (
        favorite_color(
            {
                "Sally": "blue",
                "Joe": "red",
                "John": "red",
                "Jasmine": "pink",
                "JJ": "green",
                "Penelope": "purple",
            }
        )
        == "red"
    )


def test_3_favorite_color() -> None:
    """Test edge case 1 for favorite color function."""
    assert favorite_color({}) == ""


def test_1_bin_len() -> None:
    """Test use case 1 for bin length function."""
    assert bin_len(["cat", "dog", "horse"]) == {3: {"cat", "dog"}, 5: {"horse"}}


def test_2_bin_len() -> None:
    """Test use case 2 for bin length function."""
    assert bin_len(["cow"]) == {3: {"cow"}}


def test_3_bin_len() -> None:
    """Test edge case for bin length function."""
    assert bin_len([]) == {}
