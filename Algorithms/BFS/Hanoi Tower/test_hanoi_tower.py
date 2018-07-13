import unittest
import my_hanoi

class TestStringMethods(unittest.TestCase):

    # Test of function:
    # readInitialState(filename):
    def test_reading_initial_state_from_file(self):
        expected_input = ['A', 'A', 'A', 'A']
        self.assertEqual(my_hanoi.readInitialState("data-files/teste-input.txt"), expected_input)

    # Test of function:
    # checkDisksOrder(filename)
    def test_check_disk_wrong_order(self):
        with self.assertRaises(ValueError) as context:
            my_hanoi.checkDisksOrder("data-files/teste-input-wrong-order.txt")
            self.assertTrue('Invalid State Map' in context.exception)

    # Test of function:
    # checkDisksOrder(filename)
    def test_check_disk_correct_order(self):
        self.assertTrue(my_hanoi.checkDisksOrder("data-files/teste-input.txt"))

if __name__ == '__main__':
    unittest.main()
