###
# Monthly expenses and their corresponding expense categories are included in the arrays below. 
# Write a program that calculates which expense category was the most expensive.
#

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)
max_expense_category = categories[expenses.index(max_expense)]

print('The most expensive is:', max_expense_category)