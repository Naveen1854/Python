# Vowel or Consonant using python list and Dict
DEFAULT_CHAR = 'A'
VOWEL = 'AEIOU'

VOWELS = list(VOWEL)
VOWEL_DICT = dict.fromkeys(VOWELS,'Vowel')
print(f'VOWEL List Type: {type(VOWELS)}',
      f'VOWEL Dict Type: {type(VOWEL_DICT)}', sep='\n')
print(f'VOWEL List: {VOWELS}', f"VOWEL Dict: {VOWEL_DICT}", sep='\n')

user_unput = input("Enter a single character (A-Z): ")
char = len(user_unput) == 0 and DEFAULT_CHAR or user_unput [0].upper()

char = char.isalpha() and char or DEFAULT_CHAR
print(f"\nOPTION 5: The character '{char}' is a",
      f"{char in VOWELS and 'Vowel' or 'Consonent'}.")

print(f"\nOPTIONN 6: The character '{char}' is a",
      f"{VOWEL_DICT.get(char, 'consonent')}.")