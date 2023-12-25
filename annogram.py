
print(list(filter(lambda x: x > 5, range(8))))


dog dgo -> true
dog dfo -> false
doog ddog -> fasle

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