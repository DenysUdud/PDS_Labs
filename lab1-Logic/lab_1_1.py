def first(p, q):
	"""
	Задано значення істинності висловлювань p та q. Знайти значення
	істинності кон’юнкції, диз’юнкції, альтернативного «або», імплікації й
	еквівалентності цих висловлювань.
	:param p: bool
	:param q: bool
	:return: None
	"""

	print("Кон'юнкція p і q:", conjunction(p, q))

	print("Диз'юнкція p і q:", disjunction(p, q))

	print("Альтернативне «або» p і q:", alternative(p, q))

	print("Імплікація p на q:", implication(p, q))

	print("Еквівалентність p і q:", equivalence(p, q))

def conjunction(p, q):
	return p and q

def disjunction(p, q):
	return p or q

def alternative(p, q):
	'''
	Альтернативне "або" (англ. exclusive or, позначається як XOR) є
	однією з логічних операцій між двома значеннями істинності.
	Вона повертає істину (True), якщо кількість істинних (True)
	вхідних значень дорівнює 1, а інакше повертає хибу (False).
	:param p: bool
	:param q: bool
	:return: None
	'''
	# return p ^ q
	return p != q

def implication(p, q):
	return (not p) or q

def equivalence(p, q):
	return p == q

if __name__ == "__main__":
	p = True
	q = False
	first(p, q)