def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    rok = int(input('Podaj rok: '))
    czy_rok_przestepny = (rok % 400 == 0) or (rok % 100 != 0) and (rok % 4 == 0)
    print('Czy rok', rok, 'jest przestępny?', czy_rok_przestepny)