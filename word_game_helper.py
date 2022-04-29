import pprint
import statistics
from contextlib import suppress
from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class ValidCharacter:
    definite_locations: set[int]
    definite_not_locations: set[int]


class CharacterStatus(Enum):
    GRAY = "gray"
    GREEN = "green"
    YELLOW = "yellow"


@dataclass
class CharacterGuess:
    character: str
    status: CharacterStatus


@dataclass
class GroupStats:
    answer: str
    is_potential_solution: bool
    number_of_groups: int
    average_group_size: float
    largest_group: int


class WordGameHelper:
    _eliminated_characters: set[str]
    _included_characters: dict[str, ValidCharacter]
    _original_possible_common_words: set[str]
    possible_words: set[str]
    possible_common_words: set[str]

    def __init__(
        self,
        possible_words: Optional[set[str]],
        possible_common_words: Optional[set[str]],
        used_words: Optional[set[str]],
    ):
        self._eliminated_characters = set()
        self._included_characters = {}
        self.possible_words = possible_words or set()
        self.possible_common_words = possible_common_words or set()
        self._original_possible_common_words = possible_common_words.copy()

        if used_words:
            self.possible_words = self.possible_words - used_words
            self.possible_common_words = self.possible_common_words - used_words

    def make_guess(self, guess: list[CharacterGuess]):
        for index, character_guess in enumerate(guess):
            self._update_characters(index, character_guess)

        self._update_possible_words()

    def print_possible_answers(self):
        if len(self.possible_words) == 1:
            print(f"The answer is {self.possible_words.pop().upper()}.")
            return

        # possible_answers: list[str] = list(self.possible_words)
        # possible_answers.sort()
        # print(f"There are {len(possible_answers)} possible answers.")
        # print("\n".join(possible_answers))
        # print()

        if len(self.possible_common_words) == 1:
            print(f"The answer is probably {self.possible_common_words.pop().upper()}.")
            return

        possible_common_answers: list[str] = list(self.possible_common_words)
        possible_common_answers.sort()
        print(f"There are {len(possible_common_answers)} common possible answers.")

        if len(possible_common_answers) < 5:
            print("\n".join(possible_common_answers))

        if len(possible_common_answers) > 2:
            self._get_best_guess()

    def _get_best_guess(self):
        answer_groups = {}
        statuses = [CharacterStatus.GRAY, CharacterStatus.GREEN, CharacterStatus.YELLOW]
        stats: list[GroupStats] = []

        for index, answer in enumerate(self._original_possible_common_words):
            answer_groups[answer] = []
            group_lengths = []

            for status1 in statuses:
                for status2 in statuses:
                    for status3 in statuses:
                        for status4 in statuses:
                            for status5 in statuses:
                                helper = WordGameHelper(
                                    self.possible_common_words,
                                    self.possible_common_words,
                                    set(),
                                )

                                helper.make_guess(
                                    [
                                        CharacterGuess(answer[0], status1),
                                        CharacterGuess(answer[1], status2),
                                        CharacterGuess(answer[2], status3),
                                        CharacterGuess(answer[3], status4),
                                        CharacterGuess(answer[4], status5),
                                    ]
                                )

                                if len(helper.possible_words) > 0:
                                    group = helper.possible_common_words
                                    answer_groups[answer].append(group)
                                    group_lengths.append(len(group))

            average_length = statistics.mean(group_lengths)
            group_stats = GroupStats(
                answer=answer,
                is_potential_solution=answer in self.possible_common_words,
                number_of_groups=len(group_lengths),
                average_group_size=average_length,
                largest_group=max(group_lengths),
            )
            # pprint.pprint(group_stats)
            stats.append(group_stats)

        stats.sort(key=lambda x: x.average_group_size)

        print(f"    The best guesses statistically are:")

        count: int = 0

        for stat in stats:
            if stat.average_group_size > stats[0].average_group_size:
                continue

            if count > 10:
                break

            print(
                f"        {stat.answer}, "
                f"is_potential_solution = {stat.is_potential_solution}, "
                f"number_of_groups = {stat.number_of_groups}, "
                f"average_group_size = {stat.average_group_size}, "
                f"largest_group = {stat.largest_group}"
            )

            count += 1

        print(f"    The best, possibly-correct guesses statistically are:")
        potential_solution_stats = [
            stat for stat in stats if stat.is_potential_solution
        ]

        for stat in potential_solution_stats[:10]:
            # if stat.average_group_size > potential_solution_stats[0].average_group_size:
            #     continue

            print(
                f"        {stat.answer}, "
                f"is_potential_solution = {stat.is_potential_solution}, "
                f"number_of_groups = {stat.number_of_groups}, "
                f"average_group_size = {stat.average_group_size}, "
                f"largest_group = {stat.largest_group}"
            )

    def _update_characters(self, position: int, guess: CharacterGuess):
        value = self._included_characters.get(
            guess.character, ValidCharacter(set(), set())
        )

        if (
            guess.status == CharacterStatus.GRAY
            and guess.character not in self._included_characters
        ):
            value.definite_not_locations.add(position)
            self._eliminated_characters.add(guess.character)
            return

        with suppress(KeyError):
            self._eliminated_characters.remove(guess.character)

        if guess.status in (CharacterStatus.YELLOW, CharacterStatus.GRAY):
            value.definite_not_locations.add(position)
        else:
            value.definite_locations.add(position)

        self._included_characters[guess.character] = value

    def _update_possible_words(self):
        updated_possible_words: set[str] = set()
        updated_possible_common_words: set[str] = set()

        for word in self.possible_words:
            if len(set(word).intersection(self._eliminated_characters)) > 0:
                continue

            is_valid: bool = True

            for character, valid_character in self._included_characters.items():
                if not is_valid:
                    break

                if character not in word:
                    is_valid = False
                    break

                for invalid_location in valid_character.definite_not_locations:
                    if word[invalid_location] == character:
                        is_valid = False
                        break

                for valid_location in valid_character.definite_locations:
                    if word[valid_location] != character:
                        is_valid = False
                        break

            if not is_valid:
                continue

            updated_possible_words.add(word)

            if word in self.possible_common_words:
                updated_possible_common_words.add(word)

        self.possible_words = updated_possible_words
        self.possible_common_words = updated_possible_common_words
