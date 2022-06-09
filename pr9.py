def cel_to_far(cel):
    return (cel * (9/5)) + 32


def far_to_cel(far):
    return (far - 32) / 1.8


print('What do you want to change\n')
option = int(input('1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius\n'))

if option == 1:
    ce = float(input('Enter the temperature in celsius: '))
    print(f' {ce} Celsius will be {cel_to_far(ce)} Fahrenheit.')
elif option == 2:
    fa = float(input('Enter the temperature in Fahrenheit: '))
    print(f' {fa} Fahrenheit will be {far_to_cel(fa)} Celsius.')
else:
    print('Choose the right option(1 & 2 only)')
