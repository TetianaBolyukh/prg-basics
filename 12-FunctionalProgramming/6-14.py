filled_bottles = [508,500,512,499,492,511,503,476,501,509]
incorrectly_filled = list(filter(lambda x: -10 <= x-500 <= 10, filled_bottles))
percentage = (len(filled_bottles)-len(incorrectly_filled))*100/len(filled_bottles)

print(f'Bottle capacity:    500ml')
print(f'Filling tolerance:  2%')
print(f'Filled bottles:    ',*filled_bottles)
print(f'Incorrectly filled: {percentage}%')