#week_5 
#Test Cases

import unittest
from bmi_program.py import calculate_bmi, get_bmi_category

class TestBMI(unittest.TestCase):

    # Test Case #1
    def test_normal_bmi(self):
        bmi = calculate_bmi(150, 5, 2)
        self.assertAlmostEqual(bmi, 27.4, places=1)  # Expected BMI = 27.4
        self.assertEqual(get_bmi_category(bmi), "Overweight")  # Expected category: Overweight

    # Test Case #2
    def test_underweight_bmi(self):
        bmi = calculate_bmi(90, 5, 7)
        self.assertAlmostEqual(bmi, 14.1, places=1)  # Expected BMI = 14.1
        self.assertEqual(get_bmi_category(bmi), "Underweight")  # Expected category: Underweight

    # Test Case #3
    def test_obese_bmi(self):
        bmi = calculate_bmi(250, 5, 2)
        self.assertAlmostEqual(bmi, 45.7, places=1)  # Expected BMI = 45.7
        self.assertEqual(get_bmi_category(bmi), "Obese")  # Expected category: Obese

    # Test Case #4 (Fail)
    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(100, 0, 5)  # raise an error

    # Test Case #5 (Fail)
    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            calculate_bmi(-135, 5, 8)  # raise an error

if __name__ == '__main__':
    unittest.main()

