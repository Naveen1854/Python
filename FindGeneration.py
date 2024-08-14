#Find Generation

birth_year=int(input('Enter Birth Year: '))
print(f'\nBirth year is {birth_year}',
      f'Is Baby Boomer: {birth_year >= 1946 and birth_year < 1964}',
      f'Is Gen X: {birth_year >= 1956 and birth_year < 1980}',
      f'Is Millennial: {birth_year >= 1981 and birth_year < 1996}',
      f'Is Gen Z: {birth_year >= 1997 and birth_year < 2012}',
      f'Is Gen Alpha: {birth_year >= 2013 and birth_year < 2025}', sep='\n')