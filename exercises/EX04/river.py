"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        fish_list: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                fish_list.append(fish)
        self.fish = fish_list

        bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                bear_list.append(bear)
        self.bear = bear_list
        return None

    def remove_fish(self, amount: int) -> None:
        fish_list: list[Fish] = self.fish
        idx: int = 0
        for fish in fish_list:
            if idx <= amount:
                fish_list.pop(idx)
            idx += 1
        self.fish = fish_list
        return None

    def bears_eating(self) -> None:
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(amount=3)
                bear.eat(3)
        return None

    def check_hunger(self) -> None:
        bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                bear_list.append(bear)
        self.bear = bear_list
        return None

    def repopulate_fish(self) -> None:
        pairs: int = (len(self.fish) // 2) * 4
        for fish in range(0, pairs):
            my_fish = Fish()
            self.fish.append(my_fish)
        return None

    def repopulate_bears(self):
        pairs: int = len(self.bear) // 2
        for bear in range(0, pairs):
            my_bear = Bear()
            self.bears.append(my_bear)
        return None

    def view_river(self) -> None:
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
