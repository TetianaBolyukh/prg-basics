def f(detector):
    current_people = 0
    max_people = 0
    for sign in detector:
        if sign == '+':
            current_people += 1
        elif sign == '-':
            current_people -= 1
        if current_people > max_people:
            max_people = current_people
    return max_people >= 3
print(f('+-+++-+---'))
print(f('+-+-+-+-'))
print(f('+-++-+--'))
print(f('+-++-++-+---'))