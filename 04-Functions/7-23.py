def f(password):
    if len(str(password)) >= 6:
        for i in password:
            if password.count(i) > 1:
                return False
    else:
        return False
    return True
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty") )
print(f(""))