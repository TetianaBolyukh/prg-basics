#Tip: use the Python built-in functions: map(), sum(), min(), max()
points = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

def calculate_sum(scores):
    return sum(scores) - min(scores) - max(scores)

calculated_sum = list(map(calculate_sum, points))
print(calculated_sum)