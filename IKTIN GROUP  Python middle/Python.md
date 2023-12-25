
test_data = [1 ,2, 3, [4, 5, [6, 7]]]

```python
def flat_list(mlti_list: list):
    new_list = []
    for el in mlti_list:
        if isinstance(el, list):
            new_list.extend(flat_list(el))
        else:
            new_list.append(el)
    
    return new_list


print(flat_list(test_data))
```



MRO

class Base:
	def __init__(self):
		print('Base')
		pass

class X(Base):
	def __init__(self):
		super().__init__()
		print('X')

class Y(Base):
	def __init__(self):
		super().__init__()
		print('Y')

class Z(X, Y):
	def __init__(self):
		super().__init__()
		print('Z')
		
z = Z()




words = ['aba', 'bac', 'abb', 'bab', 'bba', 'aab', 'abca', ]


def count_annogram(words: list):
  counters = {}
  for indx, word in enumerate(words):
    ordered_word = ''.join(sorted(word))
    if ordered_word not in counters.keys():
        counters[ordered_word] = []
    counters[ordered_word].append(indx)
  return_list = [words[counters[counter][0]] for counter in counters]
  
  return return_list
  
 
print(count_annogram(words))





def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

# Accept input from the user
n = int(input("Input the number of Fibonacci numbers you want to generate? "))

print("Number of first ",n,"Fibonacci numbers:")
fib = fibonacci()
for _ in range(n):
    print(next(fib),end=" ")


# [1 ,2, 3, [4, 5, [6, 7]]] -> [1 ,2, 3, 4, 5, 6, 7]

def main(input_lst):
  result = []
  for el in input_lst:
    if isinstance(el, list):
      res = main(el)
      result += res
    else:
      result.append(el)
  return result


input_lst = [1 ,2, 3, [4, 5, [6, 7]]]
print(main(input_lst))