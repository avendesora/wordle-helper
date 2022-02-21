from datasets.wordle.allowed_words import words as words
from datasets.wordle.common_words import words as common_words
from datasets.wordle.used_words import words as used_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper

GRAY: CharacterStatus = CharacterStatus.GRAY
GREEN: CharacterStatus = CharacterStatus.GREEN
YELLOW: CharacterStatus = CharacterStatus.YELLOW

GAME1: WordGameHelper = WordGameHelper(words, common_words, used_words)
GAME2: WordGameHelper = WordGameHelper(words, common_words, used_words)
GAME3: WordGameHelper = WordGameHelper(words, common_words, used_words)
GAME4: WordGameHelper = WordGameHelper(words, common_words, used_words)


def guess(word: str, statuses: list[list[CharacterStatus]]) -> None:
    if len(word) != 5 or len(statuses) != 4:
        return

    for status in statuses:
        if len(status) != 5:
            return

    GAME1.make_guess(
        [
            CharacterGuess(word[0], statuses[0][0]),
            CharacterGuess(word[1], statuses[0][1]),
            CharacterGuess(word[2], statuses[0][2]),
            CharacterGuess(word[3], statuses[0][3]),
            CharacterGuess(word[4], statuses[0][4]),
        ]
    )

    GAME2.make_guess(
        [
            CharacterGuess(word[0], statuses[1][0]),
            CharacterGuess(word[1], statuses[1][1]),
            CharacterGuess(word[2], statuses[1][2]),
            CharacterGuess(word[3], statuses[1][3]),
            CharacterGuess(word[4], statuses[1][4]),
        ]
    )

    GAME3.make_guess(
        [
            CharacterGuess(word[0], statuses[2][0]),
            CharacterGuess(word[1], statuses[2][1]),
            CharacterGuess(word[2], statuses[2][2]),
            CharacterGuess(word[3], statuses[2][3]),
            CharacterGuess(word[4], statuses[2][4]),
        ]
    )

    GAME4.make_guess(
        [
            CharacterGuess(word[0], statuses[3][0]),
            CharacterGuess(word[1], statuses[3][1]),
            CharacterGuess(word[2], statuses[3][2]),
            CharacterGuess(word[3], statuses[3][3]),
            CharacterGuess(word[4], statuses[3][4]),
        ]
    )


def main():
    guess(
        "adieu",
        [
            [YELLOW, YELLOW, GRAY, GRAY, GRAY],
            [GREEN, GRAY, GREEN, YELLOW, GRAY],
            [GREEN, GRAY, GREEN, YELLOW, GRAY],
            [GRAY, GRAY, GRAY, YELLOW, YELLOW],
        ],
    )

    guess(
        "sport",
        [
            [GRAY, GRAY, YELLOW, GREEN, GRAY],
            [GRAY, GRAY, YELLOW, GREEN, GRAY],
            [GRAY, GRAY, GRAY, GRAY, GRAY],
            [GRAY, GRAY, YELLOW, GRAY, GRAY],
        ],
    )

    guess(
        "micro",
        [
            [GRAY, GRAY, GRAY, GREEN, YELLOW],
            [GREEN, GREEN, GREEN, GREEN, GREEN],
            [YELLOW, YELLOW, GRAY, GRAY, GRAY],
            [GRAY, GRAY, GRAY, GRAY, YELLOW],
        ],
    )

    GAME1.print_possible_answers()
    GAME2.print_possible_answers()
    GAME3.print_possible_answers()
    GAME4.print_possible_answers()


if __name__ == "__main__":
    main()
