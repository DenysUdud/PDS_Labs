import io
import sys
from unittest import TestCase
from itertools import permutations, combinations
from math import factorial
from lab_4_1and2 import permutations, combinations

class PermutationsTestCase(TestCase):
	def test_permutations(self):
		# Вхідні дані
		n = 3

		# Очікуваний результат
		expected_output = [
			"123",
			"132",
			"213",
			"231",
			"312",
			"321"
		]

		# Перехоплюємо вихід на stdout
		captured_output = io.StringIO()
		sys.stdout = captured_output

		# Викликаємо функцію
		permutations(n)

		# Отримуємо отриманий результат
		output = captured_output.getvalue().strip().split('\n')

		# Перевіряємо, чи співпадають результати
		self.assertEqual(output, expected_output)


class CombinationsTestCase(TestCase):
	def test_combinations(self):
		# Вхідні дані
		n = 4
		r = 2

		# Очікуваний результат
		expected_output = [
			"[1, 2]",
			"[1, 3]",
			"[1, 4]",
			"[2, 3]",
			"[2, 4]",
			"[3, 4]"
		]

		# Перехоплюємо вихід на stdout
		captured_output = io.StringIO()
		sys.stdout = captured_output

		# Викликаємо функцію
		combinations(n, r)

		# Отримуємо отриманий результат
		output = captured_output.getvalue().strip().split('\n')

		# Перевіряємо, чи співпадають результати
		self.assertEqual(output, expected_output)

if __name__ == '__main__':
	unittest.main()
