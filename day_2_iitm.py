# -*- coding: utf-8 -*-
"""Day 2 IITM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1385I2mII09dDP9aHBhWqaBtuIJwGUZhD
"""

import qrcode
img = qrcode.make('https://colab.research.google.com/drive/1385I2mII09dDP9aHBhWqaBtuIJwGUZhD?usp=sharing')
img.save('myqr.png')

# pip install qrcode

def check_palindrome(word):
    return word

check_palindrome('Ajay')

a = 'lucky'
a[::-1]

a = 'nitin'

if a == a[::-1]:
  print(f'{a} is a Palindrome')
else:
  print(f'{a} is Not a Palindrome')

def check_palindrome(word:str):
  if type(word) == str:
    word = word.upper()
    if word == word[::-1]:
      return 'Palindrome'
    else:
      return 'Not a Plaindrome'
  else:
    return 'Invalid Data Type'

check_palindrome('harry')

a:int = 'Mohan'
print(a)

def give_fibo(n):
  fibo = [0,1]
  for i in range(n-2):
     last_num = fibo[-1]
     second_last_num = fibo[-2]
     next_num = last_num + second_last_num
     fibo.append(next_num)
  return fibo

data = [34,65,654,76,856]
print(data[-1])
print(data[-2])

def give_fibo(n):
  fibo = [0,1]
  for i in range(n-2):
     last_num = fibo[-1]
     second_last_num = fibo[-2]
     next_num = last_num + second_last_num
     fibo.append(next_num)
  return fibo

print(give_fibo(20))

def check_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return 'Not a Prime Number'
            break
            print('Happy Holi')
    else:
        return 'Prime Number'

n = 5

for i in range(1,n+1):
  print(i * '* ')

n = 5

for i in range(1,n+1):
  print(' '*(n-i) + i*'* ')

'hello' + 'World'

def print_star(n = 5, typ = 'left',shape = '*'):
  if typ  == 'left':
    space  = ''

  elif typ == 'right':
    space = '  '

  elif typ == 'mid':
    space = ' '

  for i in range(1,n+1):
    print(space*(n-i) + i*f'{shape} ')

print_star(6,'left','%')

def sum_of_n_natural_numbers(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def total_sales(*args):
  #unpacking
  result = 0
  for i in args:
    result += i
  return result

total_sales(1,2,76,56,98)

sales = [45678,63,456,347,3245]

# min(sales)

sales = [45678,63,456,2,0]
min_element = sales[0]

for i in sales[1:]:
  if i < min_element:
    min_element = i
print(min_element)

def minn(*data):
  min_ele = data[0]
  for i in data[1:]:
    if i< min_ele:
      min_ele = i
  return min_ele

minn(376,246,354,8,667,468)

# max()

company = ['ola','uber','rapido','indrive','adani','tata']

# ['#OLA','#UBER','#RAPIDO']



def add_hashtag(*company):
  result = []
  for i in company:
    result.append('#'+i.upper())
  return result

add_hashtag(*company)

def store_records(name,age,sec,roll_no,Class):
  data = {'Name':name,'Age':age,'Sec':sec,'Roll_NO':roll_no,'Class':Class}
  import pandas as pd
  result = pd.DataFrame(data,index = [0])
  return result

store_records('Mohan',21,'A',12,12)
store_records('Karan',21,'A',12,12)
store_records('Naman',21,'A',12,12)

def students_records(**kwargs):
    # print(kwargs)
    # try exception
    import pandas as pd
    try:
        result = pd.DataFrame(kwargs)
        return result
    except:
        result = pd.DataFrame(kwargs,index = [1])
        return result

students_records(Name = ['Komal','Mohan','Ajay'],
                 Age = [23,45,56],
                 Roll_No = [23,32,67],
                 Address = ['Noida','Delhi','Greater Noida'])

