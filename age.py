birth_year = int(input("Enter your year of birth: "))
if birth_year<2020:
    age = 2020 - birth_year
    print(f'You are {age} years old')
else:
    print('You do not exist')


