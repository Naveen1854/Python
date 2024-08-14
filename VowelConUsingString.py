# Vowel or Consonants using python String
DEFAULT_CHAR = 'A'
VOWEL = 'AEIOU'
user_input = input("Enter a single Character (A-Z): ")
char = len(user_input) == 0 and DEFAULT_CHAR or user_input[0].upper()
char = char.isalpha() and char or DEFAULT_CHAR
print(f"\nOPTION 3: The character '{char}' is a",
      f"{VOWEL.find(char) == 0 and 'vowel' or 'Consonant'}.")
print(f"\nOPTION 4: The character '{char}' is a",
      f"{char in VOWEL and 'Vowel' or 'Consonant'}")