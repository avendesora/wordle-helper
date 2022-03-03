from datasets.lordle.allowed_words import words
from datasets.lordle.used_words import words as used_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper


def main():
    word_game: WordGameHelper = WordGameHelper(words, words, used_words)

    word_game.make_guess(
        [
            CharacterGuess("r", CharacterStatus.YELLOW),
            CharacterGuess("o", CharacterStatus.GRAY),
            CharacterGuess("h", CharacterStatus.GRAY),
            CharacterGuess("a", CharacterStatus.YELLOW),
            CharacterGuess("n", CharacterStatus.GRAY),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("s", CharacterStatus.YELLOW),
            CharacterGuess("t", CharacterStatus.YELLOW),
            CharacterGuess("a", CharacterStatus.GREEN),
            CharacterGuess("r", CharacterStatus.YELLOW),
            CharacterGuess("k", CharacterStatus.GRAY),
        ]
    )

    # word_game.make_guess(
    #     [
    #         CharacterGuess("t", CharacterStatus.GRAY),
    #         CharacterGuess("i", CharacterStatus.GREEN),
    #         CharacterGuess("m", CharacterStatus.GRAY),
    #         CharacterGuess("e", CharacterStatus.GREEN),
    #         CharacterGuess("s", CharacterStatus.GREEN),
    #     ]
    # )
    #
    # word_game.make_guess(
    #     [
    #         CharacterGuess("s", CharacterStatus.GRAY),
    #         CharacterGuess("i", CharacterStatus.GREEN),
    #         CharacterGuess("d", CharacterStatus.GRAY),
    #         CharacterGuess("e", CharacterStatus.GREEN),
    #         CharacterGuess("s", CharacterStatus.GREEN),
    #     ]
    # )
    #
    # word_game.make_guess(
    #     [
    #         CharacterGuess("w", CharacterStatus.GRAY),
    #         CharacterGuess("i", CharacterStatus.GREEN),
    #         CharacterGuess("v", CharacterStatus.GRAY),
    #         CharacterGuess("e", CharacterStatus.GREEN),
    #         CharacterGuess("s", CharacterStatus.GREEN),
    #     ]
    # )

    word_game.print_possible_answers()


if __name__ == "__main__":
    main()
