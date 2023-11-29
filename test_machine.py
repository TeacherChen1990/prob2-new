from translator import translator
from machine import machine
import unittest


class MachineTest(unittest.TestCase):
    """ 处理器测试 """

    def setUp(self) -> None:
        print("Test beginning:")

    def tearDown(self) -> None:
        print("Test finished.")

    def test_cat(self):
        print("Testing cat")
        translator.translate('./forth/cat.fth', './forth/target')
        result = machine.start('./forth/target', './forth/cat_test.txt')
        text = ''
        with open('forth/cat_test.txt') as f:
            text = f.read()
        self.assertEqual(result, text)

    def test_hello(self):
        print("Testing hello")
        translator.translate("./forth/hello.fth", "./forth/target")
        result = machine.start("./forth/target", '')
        self.assertEqual(result, "HELLO,WORLD")

    def test_prob2(self):
        print("Testing problem2")
        translator.translate("./forth/prob2.fth", "./forth/target")
        result = machine.start("./forth/target", '')
        a, b, limit = 1, 2, 4000000
        even_sum = 0

        while a <= limit:
            if a % 2 == 0:
                even_sum += a
            a, b = b, a + b
        print("问题2答案:" + str(result))
        self.assertEqual(int(result), even_sum)


if __name__ == '__main__':
    unittest.main()
