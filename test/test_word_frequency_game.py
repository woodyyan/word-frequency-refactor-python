import unittest
import src.word_frequency.word_freq_game


class TestWordFrequencyGame(unittest.TestCase):
    def test_should_return_2_the_1_is_when_count_word_frequency_given_the_the_is(self):
        word_frequency = src.word_frequency.word_freq_game.count_word_frequency('the the is')
        self.assertEqual(word_frequency, 'the 2 \nis 1')

    def test_should_return_1_the_1_is_when_count_word_frequency_given_the_is(self):
        word_frequency = src.word_frequency.word_freq_game.count_word_frequency('the is')
        self.assertIn('the 1', word_frequency)
        self.assertIn('is 1', word_frequency)

    def test_should_return_1_the_when_count_word_frequency_given_the(self):
        word_frequency = src.word_frequency.word_freq_game.count_word_frequency('the')
        self.assertEqual(word_frequency, 'the 1')

    def test_should_return_empty_when_count_word_frequency_given_empty(self):
        word_frequency = src.word_frequency.word_freq_game.count_word_frequency('')
        self.assertEqual(word_frequency, '')

    def test_should_return_2_the_1_is_when_count_word_frequency_given_the_the_is_with_extra_space(self):
        word_frequency = src.word_frequency.word_freq_game.count_word_frequency('  the   the   is  ')
        self.assertEqual(word_frequency, 'the 2 \nis 1')
