import unittest
from lab_1_1 import conjunction, disjunction, alternative, implication, equivalence
from lab_1_2 import * 

class TestLogicOperations(unittest.TestCase):

	def test_conjunction(self):
		self.assertEqual(conjunction(True, True), True)
		self.assertEqual(conjunction(True, False), False)
		self.assertEqual(conjunction(False, True), False)
		self.assertEqual(conjunction(False, False), False)

	def test_disjunction(self):
		self.assertEqual(disjunction(True, True), True)
		self.assertEqual(disjunction(True, False), True)
		self.assertEqual(disjunction(False, True), True)
		self.assertEqual(disjunction(False, False), False)

	def test_alternative(self):
		self.assertEqual(alternative(True, True), False)
		self.assertEqual(alternative(True, False), True)
		self.assertEqual(alternative(False, True), True)
		self.assertEqual(alternative(False, False), False)

	def test_implication(self):
		self.assertEqual(implication(True, True), True)
		self.assertEqual(implication(True, False), False)
		self.assertEqual(implication(False, True), True)
		self.assertEqual(implication(False, False), True)

	def test_equivalence(self):
		self.assertEqual(equivalence(True, True), True)
		self.assertEqual(equivalence(True, False), False)
		self.assertEqual(equivalence(False, True), False)
		self.assertEqual(equivalence(False, False), True)

class TestBitwiseOperations(unittest.TestCase):

	def test_bitwise_or(self):
		self.assertEqual(bitwise_or('11001100001', '10101010011'), '11101110011')

	def test_bitwise_and(self):
		self.assertEqual(bitwise_and('11001100001', '10101010011'), '10001000001')

	def test_bitwise_xor(self):
		self.assertEqual(bitwise_xor('11001100001', '10101010011'), '01100110010')

	def test_second(self):
		output = second('11001100001', '10101010011', 11)
		self.assertIsNone(output)

if __name__ == '__main__':
	unittest.main()
