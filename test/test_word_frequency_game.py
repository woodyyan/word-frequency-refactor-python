import unittest
import src.word_frequency.word_freq_game


class TestWordFrequencyGame(unittest.TestCase):
    def test_should_return_2_the_1_is_when_count_word_frequency_given_the_the_is(self):
        word_frequency = src.word_frequency.word_freq_game.count_word_frequency('the the is')
        self.assertEqual(word_frequency, 'the 2 \nis 1')

    def test_should_return_1_the_1_is_when_count_word_frequency_given_the_is(self):
        word_frequency = src.word_frequency.word_freq_game.count_word_frequency('the is')
        self.assertEqual(word_frequency, 'the 1 \nis 1')
