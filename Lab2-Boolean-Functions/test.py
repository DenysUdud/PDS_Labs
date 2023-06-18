import unittest

def function(p, q, r):
	"""
	Function represents boolean function "p or (q -> r)"
	:param p: bool
	:param q: bool
	:param r: bool
	:return: bool
	"""
	q_implies_r = not q or r
	return p or q_implies_r


class TruthTableTest(unittest.TestCase):

	def test_truth_table(self):
		expected_table = [
			[True, True, True, True],
			[True, True, False, True],
			[True, False, True, True],
			[True, False, False, True],
			[False, True, True, True],
			[False, True, False, False],
			[False, False, True, True],
			[False, False, False, True]
		]

		table = []
		for p in [True, False]:
			for q in [True, False]:
				for r in [True, False]:
					result = function(p, q, r)
					table.append([p, q, r, result])

		self.assertEqual(table, expected_table)


if __name__ == "__main__":
	unittest.main()
