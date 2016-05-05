# TODO
# '', '' -> true
# 'AT', '' -> true
# 'ATA', 'ATT' -> false
# 'AATG', 'ATGA' -> true
# 'AATG', 'AATG' -> true
# 'AATT', 'AAT' -> false
# 'ATHG', 'ATHG' -> false


import unittest

from app.umbrella import baseComparison


class TestImplementationOne(unittest.TestCase):

    def test_two_equals_valid_bases_should_return_true(self):
        self.assertTrue(baseComparison('', ''))
        self.assertTrue(baseComparison('AATG', 'AATG'))

    def test_one_empty_base_with_another_valid_should_return_true(self):
        self.assertTrue(baseComparison('AATG', 'ATGA'))

    def test_two_bases_with_diferent_lenght_should_return_false(self):
        self.assertFalse(baseComparison('AAT', 'AATG'))

    def test_invalid_base_should_return_false(self):
        self.assertFalse(baseComparison('AATG', 'AAHG'))
        self.assertFalse(baseComparison('ATHG', 'ATHG'))

    def test_two_different_bases_should_return_false(self):
        self.assertFalse(baseComparison('ATA', 'ATT'))
