# Python3 implementation to check
# if the year is a leap year
# using macros

# Macro to check if a year
# is a leap year
def ISLP(y):
  if((y % 400 == 0) or
     (y % 100 != 0) and
     (y % 4 == 0)):
    return 1;
  else:
    return 0;

# Driver code
if __name__=='__main__':

  year = 2024;
  print(ISLP(year));