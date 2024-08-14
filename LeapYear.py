#PROG 1.1: LEAP YEAR
# Step 1: prompt user to enter a year and assign to global variable year_input
year_input = input("Enter a year: ")

# Step 2: Check if input is a digit
if year_input.isdigit():

    # Step 3: Convert input to integer and assign it to the local variable year
    year = int(year_input)

    # Step 4: Check if the year is atleast 1582 which is the start of
    # the Geogorian  calender
    if year >= 1582:

      # Step 5: Divide by 100 means centuary year (ending with 00)
      # and century year divided by 400 is leap year
      if (year % 100 == 0) and (year % 400 == 0):
          print(f'The year {year} is a leap year ')

      # Step 6: Check if the year divided by 4 and not by 100
      elif(year % 4 == 0) and (year % 100 != 0):
        print(f'The year {year} is a leap year ')
      else:
        print(f'The year {year} is not a leap year')
    else:
      print(f'The entered year {year} must be 1582 or later.')
else:
  print(f'Invalid year {year_input} entered. please enter a valid year.')