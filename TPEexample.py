import concurrent.futures

workers = 5

things = [1, 2, 3]

def f(arg1):
	print(arg1)

with concurrent.futures.ThreadPoolExecutor(max_workers = workers) as executor:
	executor.map(f, things)
