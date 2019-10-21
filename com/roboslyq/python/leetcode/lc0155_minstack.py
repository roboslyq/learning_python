from collections import OrderedDict

"""
本题的关键点是有一个辅助栈，记录当前最小值。
怎么记录当前最小值呢？使用当前值与辅助栈self.sorted_date[-1]数据相比，将较小元素放入辅助栈即可.
然后在数据栈出栈时,辅助栈也出栈即可.
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.sorted_date = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.sorted_date) > 0 and self.sorted_date[-1] < x:
            self.sorted_date.append(self.sorted_date[-1])
        else:
            self.sorted_date.append(x)

    def pop(self) -> None:
        self.sorted_date.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.sorted_date[-1]
