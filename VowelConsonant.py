# Vowel or Consonant using if and match block
DEFAULT_CHAR = 'A'
user_input = input("Enter a single character (A-Z): ")
char = len(user_input) == 0 and DEFAULT_CHAR or user_input[0].upper()
char = char.isalpha() and char or DEFAULT_CHAR
if (char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
  print(f'\nOPTION 1: The character {char} is a Vowel. ')
else:
  print(f'\nOPTION 1: The Character {char} is a Consonant. ')

match char:
  case 'A' | 'E' | 'I' | 'O' | 'U' :
    print(f'\nOPTION 2: The character {char} is a Vowel. ')
  case _:
    print(f'\nOPTION 2: The Character {char} is a Consonant. ')