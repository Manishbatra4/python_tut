# Passing Function through another Function
def add_ten(x):
    return x + 10

def twice(func, args):
    return func(func(args))

print(twice(add_ten, 10))

# Lambda Function
def sqrt(x):
    return x ** 2
print(sqrt(10))

result = (lambda x: x ** 2)(30)
print(result)

# mappig
def add(x):
    return x * 2

newlist = [10, 20, 30, 40]
result = list(map(add, newlist))
print(result)
result = list(map((lambda x: x ** 2), newlist))
print(result)

# filter
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = list(filter(lambda x: x % 2 == 0, list1))
print(result)


# generators
def even(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even(20)))
