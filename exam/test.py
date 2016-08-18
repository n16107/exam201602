import sys
import unittest

class TestTest(unittest.TestCase, StdIoHook):
class StdIoHook:
     def __init__(self):
            self.held = None

     def test_test(self):
       test.test()
       self.assertEqual(sys.stdout.getvalue(), 'ok\n')


     def test_test2(self):
       test.test()
       self.assertEqual(sys.stdout.getvalue(), 'ok\n')
       self.reset_stdout()
       test.test2()
       self.assertEqual(sys.stdout.getvalue(), 'ng\n')
