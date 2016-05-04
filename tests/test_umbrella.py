# TODO
# '', '' -> true
# 'AT', '' -> true
# 'ATA', 'ATT' -> false
# 'AATG', 'ATGA' -> true
# 'AATG', 'AATG' -> true
# 'AATT', 'AAT' -> false
# 'ATHG', 'ATHG' -> false


import unittest

from app.umbrella import Implementation1


class TestImplementation(unittest.TestCase):

    def two_empty_bases_should_return_true(self):
        self.assertTrue(baseComparison('', ''))
        self.assertTrue(baseComparison('AATG', 'ATGA'))

    def one_empty_base_with_another_valid_should_return_true(self):
        self.assertTrue(baseComparison('AATG', 'ATGA'))

    def two_bases_with_the_same_string_should_return_true(self):
        self.assertTrue(baseComparison('AATG', 'AATG'))

    def two_bases_with_diferent_lenght_should_return_false(self):
        self.assertFalse(baseComparison('AATG', 'AATG'))

    def invalid_base_should_return_false(self):
        self.assertFalse(baseComparison('AATG', 'AAHG'))
        self.assertFalse(baseComparison('ATHG', 'ATHG'))
