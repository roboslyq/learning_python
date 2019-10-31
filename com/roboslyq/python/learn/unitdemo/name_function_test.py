import unittest
from unitdemo.name_function import get_formatted_name

"""
当一个类继承unittest.TestCase类之后，所有以test_打头的方法都将自动运行。
"""


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        print("1")
        self.assertEqual(formatted_name, 'Janis Joplin')


class NamesTestCase1(unittest.TestCase):
    """测试name_function.py"""

    # 注意：紧跟函数名称的第一个(必须是第1个，并且不能换行)"""xx"""这种注释方式，可以被unittest打印在控制台上。
    def test_first_last_name(self):
        """ 能够正确地处理像Janis Joplin这样的姓名吗？--  """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis joplin')


unittest.main()
