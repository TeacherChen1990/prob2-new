from translator import translator
import unittest
import filecmp


class TranslatorTest(unittest.TestCase):
    """ 翻译测试 """

    def setUp(self) -> None:
        print("Test of translator beginning:")

    def tearDown(self) -> None:
        print("Test of translator finished.")

    def test_hello(self):
        print("Testing hello")
        translator.translate("./forth/hello.fth", "./tmp/result.tmp")
        status = filecmp.cmp('./tmp/result.tmp', './target/hello')
        self.assertEqual(status, True)

    def test_cat(self):
        print("Testing cat")
        translator.translate("./forth/cat.fth", "./tmp/result.tmp")
        status = filecmp.cmp('./tmp/result.tmp', './target/cat')
        self.assertEqual(status, True)

    def test_prob2(self):
        print("Testing problem2")
        translator.translate("./forth/prob2.fth", "./tmp/result.tmp")
        status = filecmp.cmp('./tmp/result.tmp', 'target/problem2')
        self.assertEqual(status, True)
