from datasets.wordle.allowed_words import words as words
from datasets.wordle.common_words import words as common_words
from datasets.quordle.used_words import words as used_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper

GRAY: CharacterStatus = CharacterStatus.GRAY
GREEN: CharacterStatus = CharacterStatus.GREEN
YELLOW: CharacterStatus = CharacterStatus.YELLOW

# common_words = set()

GAME1: WordGameHelper = WordGameHelper(words, common_words, used_words)
GAME2: WordGameHelper = WordGameHelper(words, common_words, used_words)
GAME3: WordGameHelper = WordGameHelper(words, common_words, used_words)
GAME4: WordGameHelper = WordGameHelper(words, common_words, used_words)

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
        "ADIEU",
        [
            [YELLOW, GRAY, GRAY, YELLOW, GRAY],
            [GRAY, GRAY, GRAY, GREEN, GRAY],
            [GRAY, GRAY, GREEN, YELLOW, GRAY],
            [YELLOW, GRAY, GRAY, YELLOW, GRAY],
        ],
    )

    guess(
        "SPORT",
        [
            [GRAY, GRAY, GRAY, YELLOW, GRAY],
            [GRAY, GRAY, GRAY, YELLOW, YELLOW],
            [GRAY, GRAY, YELLOW, GRAY, GRAY],
            [GREEN, GRAY, GRAY, YELLOW, GRAY],
        ],
    )

    guess(
        "VOICE",
        [
            [YELLOW, GRAY, GRAY, YELLOW, GREEN],
            [GRAY, GRAY, GRAY, GRAY, YELLOW],
            [YELLOW, YELLOW, GREEN, GRAY, GREEN],
            [GRAY, GRAY, GRAY, GRAY, YELLOW],
        ],
    )

    guess(
        "OLIVE",
        [
            [GRAY, GRAY, GRAY, GREEN, GREEN],
            [GRAY, GRAY, GRAY, GRAY, YELLOW],
            [GREEN, GRAY, GREEN, YELLOW, GREEN],
            [GRAY, GRAY, GRAY, GRAY, YELLOW],
        ],
    )

    guess(
        "OVINE",
        [
            [GRAY, YELLOW, GRAY, GRAY, GREEN],
            [GRAY, GRAY, GRAY, GRAY, YELLOW],
            [GREEN, GREEN, GREEN, GREEN, GREEN],
            [GRAY, GRAY, GRAY, GRAY, YELLOW],
        ],
    )

    guess(
        "CARVE",
        [
            [GREEN, GREEN, GREEN, GREEN, GREEN],
            [GRAY, GRAY, YELLOW, GRAY, YELLOW],
            None,
            [GRAY, YELLOW, YELLOW, GRAY, YELLOW],
        ],
    )

    guess(
        "ETHER",
        [
            None,
            [YELLOW, YELLOW, GRAY, GREEN, GREEN],
            None,
            [YELLOW, GRAY, GRAY, GRAY, GREEN],
        ],
    )

    guess(
        "METER",
        [
            None,
            [GREEN, GREEN, GREEN, GREEN, GREEN],
            None,
            [YELLOW, YELLOW, GRAY, GRAY, GREEN],
        ],
    )

    for game in GAMES:
        game.print_possible_answers()


if __name__ == "__main__":
    main()
