
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   stack = []
   brackets_pairs = {")":"(","}":"{","]":"["}
   for char in expression:
        if char in "({[":
           stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != brackets_pairs[char]:
                return False
           
   return not stack #True if brackets in expression are ok of False otherwise



if brackets_ok(expression1):
   print("Brackets are correct")
else:
   print("Brackets are incorrect")

if brackets_ok(expression2):
    print("Brackets are correct")
else:
    print("Brackets are incorrect")

if brackets_ok(expression3):
    print("Brackets are correct")
else:
    print("Brackets are incorrect")