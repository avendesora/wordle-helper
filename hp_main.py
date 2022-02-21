from datasets.hogwartle.allowed_words import words
from datasets.hogwartle.common_words import words as common_words
from datasets.hogwartle.used_words import words as used_words
from word_game_helper import CharacterGuess, CharacterStatus, WordGameHelper


def main():
    word_game: WordGameHelper = WordGameHelper(words, common_words, used_words)

    word_game.make_guess(
        [
            CharacterGuess("d", CharacterStatus.GRAY),
            CharacterGuess("r", CharacterStatus.GREEN),
            CharacterGuess("a", CharacterStatus.GREEN),
            CharacterGuess("c", CharacterStatus.GRAY),
            CharacterGuess("o", CharacterStatus.GRAY),
        ]
    )

    word_game.make_guess(
        [
            CharacterGuess("g", CharacterStatus.GREEN),
            CharacterGuess("r", CharacterStatus.GREEN),
            CharacterGuess("a", CharacterStatus.GREEN),
            CharacterGuess("i", CharacterStatus.GRAY),
            CharacterGuess("l", CharacterStatus.GRAY),
        ]
    )

    word_game.print_possible_answers()


if __name__ == "__main__":
    main()
