def second(string1, string2, n):
	"""
	Задано два бітові рядки довжиною n. Знайти результати виконання
	порозрядних операцій OR, AND, XOR цих рядків.
	:param string1: str - byte string
	:param string2: str - byte string
	:param n: int - length
	:return: None
	"""
	or_result = bitwise_or(string1, string2)
	and_result = bitwise_and(string1, string2)
	xor_result = bitwise_xor(string1, string2)

	# Виведення результатів
	print("Результат порозрядного OR: ", or_result)
	print("Результат порозрядного AND: ", and_result)
	print("Результат порозрядного XOR: ", xor_result)

def bitwise_or(string1, string2):
	result = ''
	for bit1, bit2 in zip(string1, string2):
		if bit1 == '1' or bit2 == '1':
			result += '1'
		else:
			result += '0'
	return result

def bitwise_and(string1, string2):
	result = ''
	for bit1, bit2 in zip(string1, string2):
		if bit1 == '1' and bit2 == '1':
			result += '1'
		else:
			result += '0'
	return result

def bitwise_xor(string1, string2):
	result = ''
	for bit1, bit2 in zip(string1, string2):
		if bit1 != bit2:
			result += '1'
		else:
			result += '0'
	return result

if __name__ == "__main__":
	n = 11
	string1 = "11001100001"
	string2 = "10101010011"
	second(string1, string2, n)

