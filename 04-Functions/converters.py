def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(cm):
    return cm * 2.54

def feet_to_cm(feet):
    return feet * 30.48

def inch_to_cm(inch):
    return inch * 0.393700787

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'2cm = {cm_to_inch(2)}inch')

