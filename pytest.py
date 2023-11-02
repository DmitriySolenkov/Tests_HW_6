from main import compare_lists, int_check
import unittest


class TestExample(unittest.TestCase):

    def test_first_list_empty(self):
        self.assertEqual(compare_lists((), (5, 6, 7)),
                         'One of lists is empty!')

    def test_second_list_empty(self):
        self.assertEqual(compare_lists((5, 6, 7), ()),
                         'One of lists is empty!')

    def test_first_list_not_int(self):
        self.assertEqual(compare_lists((4, 7, 'string'), (5, 6, 7)),
                         'One of lists contains not Integer!')

    def test_second_list_not_int(self):
        self.assertEqual(compare_lists((5, 6, 7), (3, 4, 6.12)),
                         'One of lists contains not Integer!')

    def test_first_bigger(self):
        self.assertEqual(compare_lists((1234, 6, 7, 8, 9), (1, 2, 3)),
                         'First list average is bigger!')

    def test_second_bigger(self):
        self.assertEqual(compare_lists((-5, 4, 2, -90), (2, 2, 2)),
                         'Second list average is bigger!')

    def test_equal(self):
        self.assertEqual(compare_lists((2, 3, 4), (1, 3, 5)),
                         'Both lists averages are equal!')


# if __name__ == '__main__':
#     unittest.main()
