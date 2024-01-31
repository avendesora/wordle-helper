from datasets.wordle.allowed_words import words
from datasets.wordle.common_words import words as common_words
from datasets.wordle.used_words import words as used_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper


def main():
    word_game: WordGameHelper = WordGameHelper(words, common_words, used_words)

    word_game.make_guess(
        [
            CharacterGuess("c", CharacterStatus.GRAY),
            CharacterGuess("r", CharacterStatus.GRAY),
            CharacterGuess("a", CharacterStatus.GRAY),
            CharacterGuess("n", CharacterStatus.GRAY),
            CharacterGuess("e", CharacterStatus.YELLOW),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("s", CharacterStatus.YELLOW),
            CharacterGuess("l", CharacterStatus.GRAY),
            CharacterGuess("e", CharacterStatus.YELLOW),
            CharacterGuess("p", CharacterStatus.GRAY),
            CharacterGuess("t", CharacterStatus.YELLOW),
        ]
    )

    word_game.print_possible_answers()


if __name__ == "__main__":
    main()
