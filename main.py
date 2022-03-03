from datasets.wordle.allowed_words import words
from datasets.wordle.common_words import words as common_words
from datasets.wordle.used_words import words as used_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper


def main():
    word_game: WordGameHelper = WordGameHelper(words, common_words, used_words)

    word_game.make_guess(
        [
            CharacterGuess("a", CharacterStatus.GRAY),
            CharacterGuess("u", CharacterStatus.GREEN),
            CharacterGuess("d", CharacterStatus.GRAY),
            CharacterGuess("i", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.GRAY),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("t", CharacterStatus.GRAY),
            CharacterGuess("u", CharacterStatus.GREEN),
            CharacterGuess("b", CharacterStatus.GRAY),
            CharacterGuess("e", CharacterStatus.GREEN),
            CharacterGuess("r", CharacterStatus.YELLOW),
        ]
    )

    # word_game.make_guess(
    #     [
    #         CharacterGuess("b", CharacterStatus.GRAY),
    #         CharacterGuess("r", CharacterStatus.GREEN),
    #         CharacterGuess("o", CharacterStatus.GREEN),
    #         CharacterGuess("t", CharacterStatus.YELLOW),
    #         CharacterGuess("h", CharacterStatus.GRAY),
    #     ]
    # )

    word_game.print_possible_answers()


if __name__ == "__main__":
    main()
