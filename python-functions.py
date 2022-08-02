# Challenge # 1
def sum_to(num):
  return sum(range(num+1))
print (sum_to(6))
print (sum_to(10))

# Challenge # 2
def largest(num):
  return max(num)
print (largest([1, 2, 3, 4, 0]))
print (largest([10, 4, 2, 231, 91, 54]))

# Challenge # 3
def occurrences(str1, str2):
  count = 0
  for word in str1:
    for char in word:
      if char == str2:
        count = count + 1
  return count
print(occurrences('fleep floop', 'e'))
print(occurrences('fleep floop', 'p'))
print(occurrences('fleep floop', 'ee'))
print(occurrences('fleep floop', 'fe'))

#Challenge # 4
def product(*args):
  product = 1
  for num in args:
    product = product * num
  return product
print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))