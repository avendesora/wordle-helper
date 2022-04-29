from datasets.wordle.allowed_words import words as words
from datasets.wordle.common_words import words as common_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper

N: CharacterStatus = CharacterStatus.GRAY
Y: CharacterStatus = CharacterStatus.GREEN
M: CharacterStatus = CharacterStatus.YELLOW

GAME1: WordGameHelper = WordGameHelper(words, common_words, set())
GAME2: WordGameHelper = WordGameHelper(words, common_words, set())
GAME3: WordGameHelper = WordGameHelper(words, common_words, set())
GAME4: WordGameHelper = WordGameHelper(words, common_words, set())
GAME5: WordGameHelper = WordGameHelper(words, common_words, set())
GAME6: WordGameHelper = WordGameHelper(words, common_words, set())
GAME7: WordGameHelper = WordGameHelper(words, common_words, set())
GAME8: WordGameHelper = WordGameHelper(words, common_words, set())

GAMES: list[WordGameHelper] = [GAME1, GAME2, GAME3, GAME4, GAME5, GAME6, GAME7, GAME8]


def guess(word: str, statuses: list[list[CharacterStatus]]) -> None:
    if len(word) != 5 or len(statuses) != 8:
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
            [N, N, N, M, N],
            [N, Y, M, N, M],
            [Y, Y, Y, N, Y],
            [N, N, N, N, N],
            [N, N, Y, N, N],
            [M, N, N, M, N],
            [N, M, N, N, M],
            [N, M, M, N, M],
        ],
    )

    guess(
        "TWEED",
        [
            [N, N, N, N, N],
            [N, N, Y, N, M],
            [N, N, M, N, N],
            [M, N, N, N, N],
            [Y, N, N, N, N],
            [N, N, N, N, N],
            [M, N, M, Y, N],
            [M, M, N, Y, N],
        ],
    )

    guess(
        "WATER",
        [
            [N, N, N, N, N],
            [N, M, N, M, M],
            [N, M, N, M, M],
            [N, N, M, N, N],
            [N, M, M, N, N],
            [N, N, N, N, N],
            [N, N, M, Y, M],
            [Y, Y, Y, Y, Y],
        ],
    )

    guess(
        "DREAM",
        [
            [N, N, N, N, N],
            [Y, Y, Y, Y, Y],
            [N, Y, M, M, N],
            [N, N, N, N, N],
            [N, N, N, M, N],
            [N, N, N, N, N],
            [N, M, M, N, N],
            None,
        ],
    )

    guess(
        "TOAST",
        [
            [N, Y, N, N, N],
            None,
            [N, N, Y, N, N],
            [N, Y, N, Y, Y],
            [Y, Y, Y, Y, Y],
            [N, N, N, N, N],
            [N, N, N, N, Y],
            None,
        ],
    )

    guess(
        "BERET",
        [
            [Y, N, N, N, N],
            None,
            [N, M, M, N, N],
            [N, N, N, N, Y],
            None,
            [N, N, N, N, N],
            [Y, Y, Y, Y, Y],
            None,
        ],
    )

    guess(
        "BONGO",
        [
            [Y, Y, Y, Y, Y],
            None,
            [N, N, N, N, N],
            [N, Y, N, N, N],
            None,
            [N, N, Y, N, N],
            None,
            None,
        ],
    )

    guess(
        "PINCH",
        [
            None,
            None,
            [N, N, N, M, N],
            [N, M, N, N, N],
            None,
            [Y, Y, Y, Y, Y],
            None,
            None,
        ],
    )

    guess(
        "FOIST",
        [
            None,
            None,
            [N, N, N, N, N],
            [Y, Y, Y, Y, Y],
            None,
            None,
            None,
            None,
        ],
    )

    for game in GAMES:
        game.print_possible_answers()


if __name__ == "__main__":
    main()
