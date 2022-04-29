from datasets.quordle.used_words import words as used_words
from datasets.wordle.allowed_words import words as words
from datasets.wordle.common_words import words as common_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper

GRAY: CharacterStatus = CharacterStatus.GRAY
GREEN: CharacterStatus = CharacterStatus.GREEN
YELLOW: CharacterStatus = CharacterStatus.YELLOW

# common_words = set()

GAME1: WordGameHelper = WordGameHelper(words, common_words, set())
GAME2: WordGameHelper = WordGameHelper(words, common_words, set())
GAME3: WordGameHelper = WordGameHelper(words, common_words, set())
GAME4: WordGameHelper = WordGameHelper(words, common_words, set())

GAMES: list[WordGameHelper] = [GAME1, GAME2, GAME3, GAME4]


def guess(word: str, statuses: list[list[CharacterStatus]]) -> None:
    if len(word) != 5 or len(statuses) != 4:
        return

    for index, status in enumerate(statuses):
        if not status or len(status) != 5:
            continue

        GAMES[index].make_guess(
            [
                CharacterGuess(word[0].lower(), status[0]),
                CharacterGuess(word[1].lower(), status[1]),
                CharacterGuess(word[2].lower(), status[2]),
                CharacterGuess(word[3].lower(), status[3]),
                CharacterGuess(word[4].lower(), status[4]),
            ]
        )


def main():
    guess(
        "CRANE",
        [
            [GRAY, GRAY, GRAY, GRAY, GRAY],
            [GRAY, GRAY, GRAY, YELLOW, GRAY],
            [GRAY, GREEN, GREEN, GRAY, GREEN],
            [GRAY, GRAY, GRAY, GREEN, GREEN],
        ],
    )

    guess(
        "SHONE",
        [
            [GREEN, GRAY, GREEN, GRAY, GRAY],
            [GRAY, GRAY, GRAY, YELLOW, GRAY],
            [GRAY, GRAY, GRAY, GRAY, GREEN],
            [GRAY, GREEN, GRAY, GREEN, GREEN],
        ],
    )

    guess(
        "WHINE",
        [
            [GRAY, GRAY, YELLOW, GRAY, GRAY],
            [GRAY, GRAY, YELLOW, YELLOW, GRAY],
            [GRAY, GRAY, GRAY, GRAY, GREEN],
            [GREEN, GREEN, GREEN, GREEN, GREEN],
        ],
    )

    guess(
        "SPOIL",
        [
            [GREEN, GREEN, GREEN, GREEN, GREEN],
            [GRAY, GRAY, GRAY, GREEN, GRAY],
            [GRAY, GRAY, GRAY, GRAY, GRAY],
            None,
        ],
    )

    guess(
        "GRADE",
        [
            None,
            [GRAY, GRAY, GRAY, GRAY, GRAY],
            [GREEN, GREEN, GREEN, GRAY, GREEN],
            None,
        ],
    )

    for game in GAMES:
        game.print_possible_answers()


if __name__ == "__main__":
    main()
