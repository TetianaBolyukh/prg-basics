# f("5290312400019022") returns "52**********9022"
def hide(card_number):
    if len(card_number) != 16 and card_number.isdigit() == False:
        print('Card number is incorrect')
    visible_digits1 = card_number[:2]
    visible_digits2 = card_number[-4:]
    masked_digits = '*' * (len(card_number) - len(visible_digits1 + visible_digits2))
    return visible_digits1 + masked_digits + visible_digits2