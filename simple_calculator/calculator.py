def add(*nums):
	res = 0
	for num in nums:
		res += num
	return res


def multiply(*nums):
	res = 1
	for num in nums:
		res *= num
	return res

if __name__ == '__main__':
	print(f'Multiply (1 2 3 4 5 6 7 8 9) = {multiply(1,2,3,4,5,6,7,8,9)}')
	print(f'Add (1 2 3 4 5 6 7 8 9) = {add(1,2,3,4,5,6,7,8,9)}')
