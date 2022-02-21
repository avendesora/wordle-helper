from common_five_letter_words import words as common_words
from five_letter_words import words
from used_five_letter_words import words as used_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper


def main():
    word_game: WordGameHelper = WordGameHelper(words, common_words, used_words)

    word_game.make_guess(
        [
            CharacterGuess("a", CharacterStatus.GRAY),
            CharacterGuess("u", CharacterStatus.GRAY),
            CharacterGuess("d", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.YELLOW),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("s", CharacterStatus.GRAY),
            CharacterGuess("p", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.YELLOW),
            CharacterGuess("r", CharacterStatus.YELLOW),
            CharacterGuess("t", CharacterStatus.YELLOW),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("f", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.YELLOW),
            CharacterGuess("r", CharacterStatus.YELLOW),
            CharacterGuess("t", CharacterStatus.YELLOW),
            CharacterGuess("y", CharacterStatus.GRAY),
        ]
    )

    word_game.print_possible_answers()


if __name__ == "__main__":
    main()
