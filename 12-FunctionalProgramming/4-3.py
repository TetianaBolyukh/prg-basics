import statistics
grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
filtered_g = filter(lambda x: x>2, grades)
result = statistics.mean(filtered_g)
print(round(result,1))