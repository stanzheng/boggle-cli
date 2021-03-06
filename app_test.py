"""
Test Boggle Game Logic
"""
import pytest
from app import Boggle

# pylint: disable=W0621
@pytest.fixture
def board():
    """Sets up game board"""
    state = 'oslc elai tant myse'
    wordlist = 'bsd_wordlist.txt'
    return Boggle(state, wordlist)


#  Sanity Check Tests
def test_init_parsing_input(board):
    """ Test Loading Board"""
    assert(board.matrix == [
        ['o', 's', 'l', 'c'],
        ['e', 'l', 'a', 'i'],
        ['t', 'a', 'n', 't'],
        ['m', 'y', 's', 'e']])

def test_init_words_on_board(board):
    """cross checked words possible on list"""
    assert(len(board.on_board) == 452)

def test_init_words_possible_moves(board):
    """All the connecting possibilities of a word kind of like Trie-lists"""
    assert(len(board.word_set) == 24628)


@pytest.mark.parametrize("test_word_guess, expected", [
    ('ten', True),       # Short word
    ('tan', True),       # Horizontal
    ('cite', True),      # Down
    ('caam', True),      # Diagonal and Reverse?
    ('tool', False),     # Non connecting word
    ('still', True),     # False positive
    ('elastica', True),   # Long Word
    ('satellite', True) # Long Word
])
def test_game_find_word_length(board, test_word_guess, expected):
    """Test Word guesses"""
    assert(board.check_guess(test_word_guess) == expected)

@pytest.mark.parametrize("test_word_guess, expected", [
    ('ten', 3),       # Short word
    ('tan', 3),       # Horizontal
    ('satellite', len('satellite'))
])
def test_game_find_word_length(board, test_word_guess, expected):
    """Test Word guesses"""
    assert(board.score_word(test_word_guess) == expected)
