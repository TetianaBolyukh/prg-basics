# A program that calculates RPN expressions
while True:
        expression_input = input("Enter an RPN expression: ")
        if expression_input == 'exit':
            break
        stack = []
        expression = expression_input
        expression_char = expression.split()
        for i in expression_char:
            if i.isdigit():
                stack.append(i)
            else:
                number2 = stack.pop()
                number1 = stack.pop()
                if i == '+':
                    stack.append(number1 + number2)
                elif i == '-':
                    stack.append(number1 - number2)
                elif i == '*':
                    stack.append(number1 * number2)
                elif i == '=':
                    stack.pop()
        