#PROG 1.2: LEAP YEAR FUNCTION

def check_leap_year(year_input):
  # Step 1: Check if input is a digit
  if year_input.isdigit()==False:
    return f'Invalid year {year_input} entered. please enter a valid year.'

  # Step 2: Convert input to integer and assign it to local variable year
  year = int(year_input)

  # Step 3: Check if the year is atleast 1582 which is the start of
  # the Gregorian calendar
  if year < 1582:
    return f'The entered year {year} must be 1582 or later.'

  # Step 4: Divide by 100 means century year(ending with 00)
  # and century year divided by 400 is a leap year
  if(year % 100 == 0) and (year % 400 == 0):
    return f'The year is a leap year'

  # Step 5: Check if the year is divided by 4 and not by 100
  if(year % 4 == 0) and (year % 100 != 0):
    return f'The year {year} is a leap year'

  # Step 6: Not a Leap Year
  return f'The year {year} is not a leap year'
print(check_leap_year(input("Enter a year: ")))