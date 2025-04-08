"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self) -> None:
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        self.age += 1
        self.hungerscore -= 1
        return None

    def eat(self, num_fish: int) -> None:
        self.hunger_score += num_fish
