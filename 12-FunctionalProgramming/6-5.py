arr = list(range(1,20))

result = list(filter(lambda x: x%2==0 and x%3==0, arr))
print(result)