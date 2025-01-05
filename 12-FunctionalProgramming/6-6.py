arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

format_emp = lambda emp: f' {emp[0].upper()}, {emp[1].lower()} '
formated = list(map(format_emp, arr))
for emp in formated:
   print(emp)
