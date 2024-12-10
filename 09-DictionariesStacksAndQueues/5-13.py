# A program that calculates RPN expressions
while True:
        expression_input = input("Enter an RPN expression: ")
        stack = []
        expression_char = expression_input
        for i in expression_char:
            if i.isdigit():
                stack.append(i)
            else:
                number2 = stack.pop()
                number1 = stack.pop()
                if i == '+':
                    stack.append(int(number1) + int(number2))
                elif i == '-':
                    stack.append(int(number1) - int(number2))
                elif i == '*':
                    stack.append(int(number1) * int(number2))
                elif i == '=':
                    stack.pop()
        print(stack.pop())
        if expression_input == 'exit':
            print('exiting...')
            break