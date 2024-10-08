# Function to create a list from a string of comma-separated values
def create_list(csv_string):
    L = csv_string.split(', ')
#    index = 0
#    for s in L:
#        L[index] = s.replace(" ", "")
#        index += 1
    return L

# Function to concatenate two lists without using +
def concatenate_lists(lst1, lst2):
    for val in lst2:
      lst1.append(val)
    return lst1
    # TODO: Implement concatenation using loops

# Function to multiply each element in a list by a scalar without using *
def scalar_multiply(lst, scalar):
    for val in range(len(lst)):
      lst[val] *= 2
    return lst

    # TODO: Implement multiplication using loops

assert create_list("apple, banana, cherry") == ["apple", "banana", "cherry"]
assert concatenate_lists([1, 2], [3, 4]) == [1, 2, 3, 4]
assert scalar_multiply([2, 3], 2) == [4, 6]
#################################################################################
'''
In the cell below, for instance, you'll find a stubbed out function named is_perfect, which should return True if the number passed to it is a "perfect" number, and False otherwise.

A perfect number is a postive integer whose value is equal to the sum of its proper divisors (i.e., its factors excluding the number itself). 6 is the first perfect number, as its divisors 1, 2, and 3 add up to 6.

Fill in your own implementation of the function below:
'''
def is_perfect(n):
    L = []
    sum = 0
    for x in range(n):
      if x == 0:
        continue
      if n % x == 0:
        L.append(x)
    for val in L:
      sum += val
    if sum == n:
      return True
    return False

#################################################################################
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Complete the following function, which finds the sum of all the multiples of 3 or 5 below the argument n.
'''
def multiples_of_3_and_5(n):
    L = []
    sum = 0
    for x in range(n):
        if(x % 3 == 0 or x % 5 ==0):
            L.append(x)
    for val in L:
        sum += val
    return sum

# (3 points)


#################################################################################
'''
Exercise 3: Integer Right Triangles
Given a perimeter of 60, we can find two right triangles with integral length sides: [(10, 24, 26), (15, 20, 25)]. Complete the following function, which takes an integer p and returns the number of unique integer right triangles with perimeter p.

Note that your solution should take care to limit the number of triangles it tests --- your function must complete in under 3 seconds for all values of p used in the tests to earn credit.
'''
def integer_right_triangles(p):
    triangles = 0
    for x in range(1,p):
      for y in range(x, p):
        if (x**2 + y**2 == (p - x - y)**2):
          triangles += 1
    return triangles

#################################################################################

def test1():
    assert is_perfect(6) == True
    assert is_perfect(28) == True
    assert is_perfect(496) == True
    assert is_perfect(1) == False
    assert is_perfect(2) == False
    assert is_perfect(3) == False
    assert is_perfect(4) == False
    assert is_perfect(5) == False
    assert is_perfect(10) == False
    assert is_perfect(20) == False

#################################################################################
# EXERCISE 2
#################################################################################

# (3 points)
def test2():
    assert multiples_of_3_and_5(10) == 23
    assert multiples_of_3_and_5(500) == 57918
    assert multiples_of_3_and_5(1000) == 233168

#################################################################################
# EXERCISE 3
#################################################################################

def test3():
    assert integer_right_triangles(60) == 2
    assert integer_right_triangles(100) == 0
    assert integer_right_triangles(180) == 3
    
def main():
    test1()
    test2()
    test3()

main()
