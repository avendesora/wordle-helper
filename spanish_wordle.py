from datasets.spanish.allowed_words import words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper


def main():
    word_game: WordGameHelper = WordGameHelper(words, words, set())

    word_game.make_guess(
        [
            CharacterGuess("a", CharacterStatus.GRAY),
            CharacterGuess("d", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.YELLOW),
            CharacterGuess("s", CharacterStatus.GRAY),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("t", CharacterStatus.GRAY),
            CharacterGuess("e", CharacterStatus.GRAY),
            CharacterGuess("n", CharacterStatus.GRAY),
            CharacterGuess("g", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.GREEN),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("u", CharacterStatus.YELLOW),
            CharacterGuess("m", CharacterStatus.GRAY),
            CharacterGuess("b", CharacterStatus.GRAY),
            CharacterGuess("r", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.GREEN),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("c", CharacterStatus.GRAY),
            CharacterGuess("h", CharacterStatus.GRAY),
            CharacterGuess("u", CharacterStatus.GREEN),
            CharacterGuess("p", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.GREEN),
        ]
    )

    word_game.print_possible_answers()


if __name__ == "__main__":
    main()
