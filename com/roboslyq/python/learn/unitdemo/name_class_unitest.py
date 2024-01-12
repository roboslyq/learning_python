import unittest
import name_class as user
from name_function import get_formatted_name


class TestDev(unittest.TestCase):

    def test_user_name(self):
        """测试name_function.py"""
        """测试name_function.py"""
        print("1")
        userentity = user.User()
        print(userentity.print_id())
        print(userentity.print_name())
        print(userentity.print_all())
        self.assertEqual(userentity.print_id(), "1")


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def setUp(self):
        self.col1 = "运行测试案例之前，先运行setUp方法"

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        print("1")
        print(self.col1)
        self.assertNotEqual(formatted_name, 'Janis Joplin')


# python3的写法
if __name__ == '__main__':
    unittest.main()
