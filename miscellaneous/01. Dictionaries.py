person = {"hello": "world", "fuk": "yeah"}
print(person["fuk"])

numbers = {
    1: "ONE",
    2: "TWO",
    3: "THREE"
}

print(numbers[1])
print(1 in numbers)
print(5 in numbers)
print(numbers.get(2))
print(numbers.get(5))
print(numbers.get(5, "Key Not Found"))
numbers.update({4: "Fourth"})
print(numbers)
print(numbers.get(4))
print(numbers.pop(3))
print(numbers)
print(numbers.clear())
print(numbers)
