from dataclasses import dataclass
from enum import Enum
from typing import Optional

from common_five_letter_words import common_words as common_five_letter_words
from five_letter_words import words as five_letter_words
from used_five_letter_words import used_words as used_five_letter_words


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


class WordGame:
    _eliminated_characters: set[str]
    _included_characters: dict[str, ValidCharacter]
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
        self.possible_words = possible_words if possible_words else set()
        self.possible_common_words = (
            possible_common_words if possible_common_words else set()
        )

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

        possible_answers: list[str] = list(self.possible_words)
        possible_answers.sort()
        print(f"There are {len(possible_answers)} possible answers.")
        print("\n".join(possible_answers))
        print()

        if len(self.possible_common_words) == 1:
            print(f"The answer is probably {self.possible_common_words.pop().upper()}.")
            return

        possible_common_answers: list[str] = list(self.possible_common_words)
        possible_common_answers.sort()
        print(f"There are {len(possible_common_answers)} common possible answers.")
        print("\n".join(possible_common_answers))

    def _update_characters(self, position: int, guess: CharacterGuess):
        if guess.status == CharacterStatus.GRAY:
            self._eliminated_characters.add(guess.character)
            return

        value = self._included_characters.get(
            guess.character, ValidCharacter(set(), set())
        )

        if guess.status == CharacterStatus.YELLOW:
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


def main():
    word_game: WordGame = WordGame(
        five_letter_words,
        common_five_letter_words,
        used_five_letter_words
    )

    # Guess #1 - ADIEU
    word_game.make_guess(
        [
            CharacterGuess("a", CharacterStatus.GRAY),
            CharacterGuess("d", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.YELLOW),
            CharacterGuess("e", CharacterStatus.GRAY),
            CharacterGuess("u", CharacterStatus.GRAY),
        ]
    )

    # Guess #2 - STRIP
    word_game.make_guess(
        [
            CharacterGuess("s", CharacterStatus.GRAY),
            CharacterGuess("t", CharacterStatus.GRAY),
            CharacterGuess("r", CharacterStatus.YELLOW),
            CharacterGuess("i", CharacterStatus.GREEN),
            CharacterGuess("p", CharacterStatus.GRAY),
        ]
    )
    word_game.print_possible_answers()


if __name__ == "__main__":
    main()
