import math
import unittest

class ExamTest(unittest.TestCase, StdIoHook):

      def test_prime_number(self):

         exam.prime_number(2)
         self.assertEqual(sys.stdout.getvalue(), 'ng\n')
         self.reset_stdout()
         exam.prime_number(3)
         self.assertEqual(sys.stdout.getvalue(), 'ok\n')
         self.reset_stdout()
         exam.prime_number(4)
         self.assertEqual(sys.stdout.getvalue(), 'ng\n')
         self.reset_stdout()
         exam.prime_number(5)
         self.assertEqual(sys.stdout.getvalue(), 'ok\n')
         self.reset_stdout()
         exam.prime_number(6)
         self.assertEqual(sys.stdout.getvalue(), 'ng\n')
         self.reset_stdout()
         exam.prime_number(7)
         self.assertEqual(sys.stdout.getvalue(), 'ok\n')
         self.reset_stdout()
         exam.prime_number(8)
         self.assertEqual(sys.stdout.getvalue(), 'ng\n')
         self.reset_stdout()
         exam.prime_number(9)
         self.assertEqual(sys.stdout.getvalue(), 'ng\n')
         self.reset_stdout()
         exam.prime_number(10)
         self.assertEqual(sys.stdout.getvalue(), 'ng\n')
         self.reset_stdout()
         exam.prime_number(11)
         self.assertEqual(sys.stdout.getvalue(), 'ok\n')

         pass


# 1からnumberまでの合計を出力してください
      def test_sum_from_1_to(self):
         exam.sum_from_1_to(1)
         self.assertEqual(sys.stdout.getvalue(), '1\n')
         self.reset_stdout()
         exam.sum_from_1_to(5)
         self.assertEqual(sys.stdout.getvalue(), '15\n')
         self.reset_stdout()
         exam.sum_from_1_to(1000)
         self.assertEqual(sys.stdout.getvalue(), '500500\n')
         self.reset_stdout()
         exam.sum_from_1_to(777)
         self.assertEqual(sys.stdout.getvalue(), '302253\n')
         self.reset_stdout()

         pass



# numberの階乗(factorial)を出力してください
      def test_factorial(self):
          exam.factorial(0)
          self.assertEqual(sys.stdout.getvalue(), '1\n')
          self.reset_stdout()
          exam.factorial(4)
          self.assertEqual(sys.stdout.getvalue(), '24\n')
          self.reset_stdout()
          exam.factorial(9)
          self.assertEqual(sys.stdout.getvalue(), '362880\n')
          self.reset_stdout()
          exam.factorial(13)
          self.assertEqual(sys.stdout.getvalue(), '6227020800\n')
          self.reset_stdout()
          exam.factorial(7)
          self.assertEqual(sys.stdout.getvalue(), '5040\n')
          self.reset_stdout()

          pass


# リストdataの各要素(整数)を3乗した結果をリスト型として返してください
      def test_cubic_list(self):
         self.assertEqual(
         exam.cubic_list([1, 2, 3, 4, 5]), [1, 8, 27, 64, 125])
         self.assertEqual(exam.cubic_list(
          [-3, -2, -1, 0, 1, 2, 3]), [-27, -8, -1, 0, 1, 8, 27])

         pass


# 底辺x,高さyの直角三角形(right angled triangle)の残り1つの辺の長さを返してください
      def test_calc_hypotenuse(self):
         self.assertEqual(exam.calc_hypotenuse(1, 2), math.sqrt(5))
         self.assertEqual(exam.calc_hypotenuse(3, 4), 5.0)
         self.assertEqual(exam.calc_hypotenuse(9, 12), 15.0)

         pass


# 底辺x,斜辺vの直角三角形の残り1つの辺の長さを返してください
      def test_calc_subtense(self):
         self.assertEqual(exam.calc_subtense(15, 12), 9)
         self.assertEqual(exam.calc_subtense(5, 3), 4)
         self.assertEqual(exam.calc_subtense(1, 2), math.sqrt(3))

         pass


# 三辺の長さがそれぞれx,y,zの三角形の面積を返してください
      def test_calc_area_triangle(self):
         self.assertEqual(exam.calc_area_triangle(3, 4, 5), 6)
         self.assertEqual(exam.calc_area_triangle(9, 12, 15), 54)
         self.assertEqual(exam.calc_area_triangle(10, 15, 20), 72.61843774138907)

         pass


# 引数a,b,cを小数点以下2桁表示で空白切りで表示してください
      def test_point_two_digits(self):
         exam.point_two_digits(1.4142135623730951, 1.7320508075688772, 2.23606797749979)
         self.assertEqual(sys.stdout.getvalue(), '1.41 1.73 2.24\n')
         self.reset_stdout()
         exam.point_two_digits(2.449489742783178, 2.6457513110645907, 2.8284271247461903)
         self.assertEqual(sys.stdout.getvalue(), '2.45 2.65 2.83\n')
         self.reset_stdout()
         exam.point_two_digits(2, 3, 4)
         self.assertEqual(sys.stdout.getvalue(), '2.00 3.00 4.00\n')
         self.reset_stdout()

         pass


# リストdataの内容を小さい順でソートした結果を返してください
      def test_list_sort(self):
         self.assertEqual(exam.list_sort([1, 2, 3, 4]), [1, 2, 3, 4])
         self.assertEqual(exam.list_sort([4, 3, 2, 1]), [1, 2, 3, 4])
         self.assertEqual(exam.list_sort([3, 3, 2, 9]), [2, 3, 3, 9])
         self.assertEqual(exam.list_sort([-1, -2, -3, -4]), [-4, -3, -2, -1])
         pass


# 文字列の並びを逆にしたものを返してください
      def test_reverse_string(self):
         self.assertEqual(exam.reverse_string('hello, python'), 'nohtyp ,olleh')
         self.assertEqual(exam.reverse_string('dive into python 3'), '3 nohtyp otni evid')

         pass


# dateから2016年4月1日までの日数を返してください
      def test_days_from_date(self):
         self.assertEqual(exam.days_from_date(date(1969, 12, 25)), 16899)
         self.assertEqual(exam.days_from_date(date(2001, 4, 1)), 5479)
         self.assertEqual(exam.days_from_date(date(2015, 4, 1)), 366)  # 'hello, {name}!'と出力してください 。

         pass

import sys

class ExamTest(unittest.TestCase, StdIoHook):

    def setUp(self):
         self.set_hook_stdout()

    def tearDown(self):
         self.release_hook_stdout()

    def test_hello(self):
         exam.hello('john')
         self.assertEqual(sys.stdout.getvalue(), 'hello, john!\n')

         pass

# sentence の文字数を出力してください
    def test_length(self):
         exam.length('Dive into python3!')
         self.assertEqual(sys.stdout.getvalue(), '18!\n')
         pass


   # sentence の2文字目から5文字目まで(5文字目は含まない)を出力してください
    def test_slicing2to5(self):
         exam.slicing2to5('Dive into python3!')
         self.assertEqual(sys.stdout.getvalue(), 've\n')

         pass


# number の符号を出力してください。ただし、0は'0'と出力してください
    def test_number_sign(self):
         exam.number_sign(0)
         self.assertEqual(sys.stdout.getvalue(), '0\n')

         pass


# number が素数なら'ok',そうでないなら'ng'と出力してください
    def test_prime_number(self):
         exam.prime_number(2)
         self.assertEqual(sys.stdout.getvalue(), 'ng\n')

         pass
