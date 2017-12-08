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
