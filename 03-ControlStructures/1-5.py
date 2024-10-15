###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = int(input("Enter total tasks: "))
tasks_ok = total_tasks*0.5
test_passed = False

if total_tasks >= tasks_ok:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')