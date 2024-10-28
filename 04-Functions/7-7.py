
def f(binary_number):
    for number in binary_number:
        if number != '1' and number != '0':
             return False
    return True
def main():
     binary_numbers = '101101', '1311a10100'
     for number in binary_numbers:
          print(f'{number}: {f(number)}')
if __name__ == "__main__":
     main()