
import unittest
from letter_combinations import letter_combinations, quick_sort


class TestLetterCombinations(unittest.TestCase):
    """
    Unit test class for testing the letter_combinations function and quick_sort function.
    """
    
    def test_multiple_inputs(self):
        """Test case for two-digit input (example 1 from the problem)."""
        digits = "23"
        expected_output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        result = letter_combinations(digits)
        self.assertEqual(result, expected_output)
 
    def test_empty_input(self):
        """Test case for empty input string (example 2 from the problem)."""
        digits = ""
        expected_output = []
        result = letter_combinations(digits)
        self.assertEqual(result, expected_output)
 
    def test_single_digit_input(self):
        """Test case for single digit input (example 3 from the problem)."""
        digits = "2"
        expected_output = ["a", "b", "c"]
        result = letter_combinations(digits)
        self.assertEqual(result, expected_output)

    def test_digit_7_9_has_four_letters(self):
        """
        Digit 7 and 9 map to four letters each.
        Their combinations should reflect that, resulting in 16 combinations for "79".
        """
        digits = "79"
        result = letter_combinations(digits)
        self.assertEqual(len(result), 16)
        self.assertIn("pw", result)
        self.assertIn("sz", result)

    def test_three_digit_input(self):
        """
        Three-digit input — verifies the recursion works beyond two levels.
        The length of the output should be 3 * 3 * 3 = 27 combinations for "234".
        """
        digits = "234"
        result = letter_combinations(digits)
        self.assertEqual(len(result), 27)
        self.assertIn("adg", result)
        self.assertIn("cfi", result)
 
    def test_max_length_four_digits(self):
        """
        Four digits is the maximum allowed length per the constraints.
        The length of the output should be 3 * 3 * 3 * 3 = 81 combinations for "2345".
        """
        digits = "2345"
        result = letter_combinations(digits)
        self.assertEqual(len(result), 81)
    
    def test_quick_sort_unsorted(self):
        """Quick sort must correctly order an unsorted list."""
        arr = ["b", "a", "c"]
        expected_output = ["a", "b", "c"]
        self.assertEqual(quick_sort(arr), expected_output)


    def test_quick_sort_already_sorted(self):
        """Quick sort must handle an already-sorted list without error."""
        arr = ["a", "b", "c"]
        self.assertEqual(quick_sort(arr), ["a", "b", "c"])
 
    def test_quick_sort_empty_list(self):
        """Quick sort must handle an empty list."""
        self.assertEqual(quick_sort([]), [])

    def test_quick_sort_mixed_strings(self):
        """Quick sort must correctly sort a list of strings that are not in order."""
        arr = ["bf", "ad", "ce", "ae", "cd", "bd", "af", "be", "cf"]
        self.assertEqual(quick_sort(arr), sorted(arr))

if __name__ == "__main__":
    unittest.main()
 