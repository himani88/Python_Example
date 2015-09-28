'''
Complete this function that transforms a list of integers.

1)  For numbers that are multiples of three replace the integer with the string "Fizz".

2)  For numbers that are multiples of five replace the integer with the string "Buzz".

3)  For numbers that are multiples of both three AND five replace the integer
    with the string "FizzBuzz"

Your function should take in a list of integers as input.
Your function should not modify the input list.
Your function should return an updated list with integers and strings.
'''

def fizzbuzz(intList):
	
	result = ['FizzBuzz' if x%3==0 and x%5==0 else 'Fizz' if x%3==0   else 'Buzz' if x%5==0 else x for x in intList]
    return result