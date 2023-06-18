def function(p, q, r):
	"""
	Function represents boolean function "p or (q -> r)"
	:param p: bool
	:param q: bool
	:param r: bool
	:return: bool
	"""
	q_implies_r = not q or r
	return (p or q_implies_r)


def truth_table():
	"""
	1. Побудувати таблицю істинності для функції f n , заданої
	формулою (n – номер варіанту) "p or (q -> r)"
	:return: None
	"""
	variables = ['n', 'p', 'q', 'r']
	table = []

	for p in [True, False]:
		for q in [True, False]:
			for r in [True, False]:
				result = function(p, q, r)
				table.append([p, q, r, result])

	# Виводимо таблицю істинності
	headers = variables + ['f']
	print('|', end='')
	for header in headers:
		print(f' {header} |', end='')
	print()

	for row in table:
		print('|', end='')
		for value in row:
			print(f' {value} |', end='')
		print()

if __name__ == "__main__":
	truth_table()
