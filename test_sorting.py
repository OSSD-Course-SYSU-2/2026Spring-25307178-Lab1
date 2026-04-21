import unittest

from sorting import parse_numbers, sort_numbers


class SortNumbersTests(unittest.TestCase):
    def test_sorts_unsorted_values(self):
        self.assertEqual(sort_numbers([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_handles_duplicates_and_negative_numbers(self):
        self.assertEqual(sort_numbers([3, -1, 3, 0, -5]), [-5, -1, 0, 3, 3])

    def test_returns_new_sorted_list(self):
        original = [2, 1]
        result = sort_numbers(original)
        self.assertEqual(result, [1, 2])
        self.assertEqual(original, [2, 1])

    def test_handles_empty_input(self):
        self.assertEqual(sort_numbers([]), [])

    def test_parses_numbers_from_text_input(self):
        self.assertEqual(parse_numbers(["7", "-2", "0"]), [7, -2, 0])


if __name__ == "__main__":
    unittest.main()
