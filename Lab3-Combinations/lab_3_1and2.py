def permutation_count(n, r):
	"""
	Обчислює кількість усіх розміщень без повторень з n елементів по r.
	:param n: int, кількість елементів
	:param r: int, кількість елементів у розміщенні
	:return: int, кількість розміщень
	"""
	if n < r:
		return 0
	result = 1
	for i in range(r):
		result *= (n - i)
	return result

def stirling_and_bell(i):
	n = i + 5

	F = [[0] * (n + 1) for _ in range(n + 1)]
	for j in range(1, n + 1):
		F[j][1] = 1
		F[j][j] = 1

	for j in range(3, n + 1):
		for k in range(2, j):
			F[j][k] = F[j - 1][k - 1] + k * F[j - 1][k]

	B = [0] * (n + 1)
	B[1] = 1

	for j in range(2, n + 1):
		for k in range(1, j + 1):
			B[j] += F[j][k]

	print("Stirling numbers of the second kind:")
	for j in range(1, n + 1):
		for k in range(1, j + 1):
			print(F[j][k], end="\t")
		print()

	print("Bell numbers:")
	for j in range(1, n + 1):
		print(B[j], end="\t")

def main():
	n = 5
	r = 4
	permutations = permutation_count(n, r)
	print(f"Кількість розміщень без повторень з {n} елементів по {r}: {permutations}")

	i = 11
	stirling_and_bell(i)


if __name__ == '__main__':
	main()
