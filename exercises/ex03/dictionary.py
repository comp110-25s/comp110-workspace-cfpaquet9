"""Dictionary Functions."""

__author__ = "730515621"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    result = dict[str, str]()

    for key in my_dictionary:
        value: str = my_dictionary[key]
        if value in result:
            raise KeyError("Duplicate Key")
        result[value] = key
    return result


def count(a: list[str]) -> dict[str, int]:
    result = dict[str, int]()
    idx_a: int = 0

    while idx_a < len(a):
        if a[idx_a] in result:
            result[a[idx_a]] += 1
        else:
            result[a[idx_a]] = 1
        idx_a += 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    result: list[str] = []

    for key in colors:
        result.append(colors[key])
    colorsdict: dict[str, int] = count(result)

    fav: str = ""
    votes: int = 0
    for key in colorsdict:
        if colorsdict[key] > votes:
            fav = key
            votes = colorsdict[key]
    return fav


def bin_len(bins: list[str]) -> dict[int, set[str]]:
    result: dict[int, set[str]] = dict()

    idx: int = 0
    while idx < len(bins):
        word: str = bins[idx]
        if len(word) in result:
            result[len(word)].add(word)
        else:
            result[len(word)] = {word}

        idx += 1

    return result
