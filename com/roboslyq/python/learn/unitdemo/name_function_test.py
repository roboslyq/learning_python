import unittest

from unitdemo.name_class import User as user
from unitdemo.name_function import get_formatted_name

"""
当一个类继承unittest.TestCase类之后，所有以test_打头的方法都将自动运行。
"""


class Test1(unittest.TestCase):
    def test_user(self):
        user_entity1 = user("1", "luoyq")
        print(user_entity1.print_id(), "1")
        self.assertEqual(user_entity1.print_id(), "1")


unittest.main()
