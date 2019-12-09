# -*- coding: utf-8 -*-

def fibonacci(op_number):
  fibonacci_numbers = [1, 1]
  try:
    for numbers in range(op_number):
      if op_number > 2:
        fibonacci_numbers.append(int(fibonacci_numbers[-1] + int(fibonacci_numbers[-2])))
    print(fibonacci_numbers[0:int(op_number)])
  except:
    print('Please enter an integer!')

fibonacci('Enter the number of elements you would like to see in the list')
