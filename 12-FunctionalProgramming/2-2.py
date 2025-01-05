names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
sort = lambda names: sorted(names, key=len)
result = sort(names)
print(result)