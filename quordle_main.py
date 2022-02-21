from common_five_letter_words import words as common_five_letter_words
from five_letter_words import words as five_letter_words
from used_five_letter_words import words as used_five_letter_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper


def main():
    word_game: WordGameHelper = WordGameHelper(
        five_letter_words, common_five_letter_words, used_five_letter_words
    )
    word_game2: WordGameHelper = WordGameHelper(
        five_letter_words, common_five_letter_words, used_five_letter_words
    )
    word_game3: WordGameHelper = WordGameHelper(
        five_letter_words, common_five_letter_words, used_five_letter_words
    )
    word_game4: WordGameHelper = WordGameHelper(
        five_letter_words, common_five_letter_words, used_five_letter_words
    )

    word_game.make_guess(
        [
            CharacterGuess("a", CharacterStatus.YELLOW),
            CharacterGuess("d", CharacterStatus.YELLOW),
            CharacterGuess("i", CharacterStatus.GRAY),
            CharacterGuess("e", CharacterStatus.GRAY),
            CharacterGuess("u", CharacterStatus.GRAY),
        ]
    )

    word_game2.make_guess(
        [
            CharacterGuess("a", CharacterStatus.GRAY),
            CharacterGuess("d", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.YELLOW),
            CharacterGuess("e", CharacterStatus.GRAY),
            CharacterGuess("u", CharacterStatus.GRAY),
        ]
    )

    word_game3.make_guess(
        [
            CharacterGuess("a", CharacterStatus.GREEN),
            CharacterGuess("d", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.GREEN),
            CharacterGuess("e", CharacterStatus.YELLOW),
            CharacterGuess("u", CharacterStatus.GRAY),
        ]
    )

    word_game4.make_guess(
        [
            CharacterGuess("a", CharacterStatus.GRAY),
            CharacterGuess("d", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.GRAY),
            CharacterGuess("e", CharacterStatus.YELLOW),
            CharacterGuess("u", CharacterStatus.YELLOW),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("s", CharacterStatus.GRAY),
            CharacterGuess("p", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.YELLOW),
            CharacterGuess("r", CharacterStatus.GREEN),
            CharacterGuess("t", CharacterStatus.GRAY),
        ]
    )

    word_game2.make_guess(
        [
            CharacterGuess("s", CharacterStatus.GRAY),
            CharacterGuess("p", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.YELLOW),
            CharacterGuess("r", CharacterStatus.GREEN),
            CharacterGuess("t", CharacterStatus.GRAY),
        ]
    )

    word_game3.make_guess(
        [
            CharacterGuess("s", CharacterStatus.GRAY),
            CharacterGuess("p", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.GRAY),
            CharacterGuess("r", CharacterStatus.GRAY),
            CharacterGuess("t", CharacterStatus.GRAY),
        ]
    )

    word_game4.make_guess(
        [
            CharacterGuess("s", CharacterStatus.GRAY),
            CharacterGuess("p", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.YELLOW),
            CharacterGuess("r", CharacterStatus.GRAY),
            CharacterGuess("t", CharacterStatus.GRAY),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("m", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.GRAY),
            CharacterGuess("c", CharacterStatus.GRAY),
            CharacterGuess("r", CharacterStatus.GREEN),
            CharacterGuess("o", CharacterStatus.YELLOW),
        ]
    )

    word_game2.make_guess(
        [
            CharacterGuess("m", CharacterStatus.GREEN),
            CharacterGuess("i", CharacterStatus.GREEN),
            CharacterGuess("c", CharacterStatus.GREEN),
            CharacterGuess("r", CharacterStatus.GREEN),
            CharacterGuess("o", CharacterStatus.GREEN),
        ]
    )

    word_game3.make_guess(
        [
            CharacterGuess("m", CharacterStatus.YELLOW),
            CharacterGuess("i", CharacterStatus.YELLOW),
            CharacterGuess("c", CharacterStatus.GRAY),
            CharacterGuess("r", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.GRAY),
        ]
    )

    word_game4.make_guess(
        [
            CharacterGuess("m", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.GRAY),
            CharacterGuess("c", CharacterStatus.GRAY),
            CharacterGuess("r", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.YELLOW),
        ]
    )

    word_game.print_possible_answers()
    word_game2.print_possible_answers()
    word_game3.print_possible_answers()
    word_game4.print_possible_answers()


if __name__ == "__main__":
    main()
