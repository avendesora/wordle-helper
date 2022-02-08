from dataclasses import dataclass

from five_letter_words import words as five_letter_words


@dataclass
class ValidCharacter:
    character: str
    definite_locations: set[int]
    definite_not_locations: set[int]


ELIMINATED_CHARACTERS = {
    "a",
    "i",
    "u",
}

INCLUDED_CHARACTERS = [
    ValidCharacter(
        "d",
        {2},
        {0, 1, 3, 4}
    ),
    ValidCharacter(
        "e",
        {0, 3},
        {2}
    ),
    ValidCharacter(
        "r",
        {4},
        {2, 3}
    )
]


def print_possible_words():
    possible_words = []

    for word in five_letter_words:
        if len(set(word).intersection(ELIMINATED_CHARACTERS)) > 0:
            continue

        is_valid: bool = True

        for valid_character in INCLUDED_CHARACTERS:
            if not is_valid:
                break

            if valid_character.character not in word:
                is_valid = False
                break

            for invalid_location in valid_character.definite_not_locations:
                if word[invalid_location] == valid_character.character:
                    is_valid = False
                    break

            for valid_location in valid_character.definite_locations:
                if word[valid_location] != valid_character.character:
                    is_valid = False
                    break

        if not is_valid:
            continue

        possible_words.append(word)

    possible_words.sort()
    print("\n".join(possible_words))


def main():
    print_possible_words()


if __name__ == "__main__":
    main()
