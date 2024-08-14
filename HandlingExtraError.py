#Good
def calculate_sum(x:int, y:int):
    """
    Returns the Sum of Two Numbers
    """
    return x + y

  #Good
  #Handling the exact Error Occured
try:
  total_sum=int(input('Enter value of total sum '))
  bonus_points=int(input('Enter value of bonus_points '))
  print(f'Data Type of total_sum is {type(total_sum)} and \n' +
        f'bonus_points is {type(bonus_points)}')
  final_score=calculate_sum(total_sum,bonus_points)
  print(f'Final score is {final_score}')
except ValueError as err:
    print(f'Oops! Got Error: {err}, \n That was no valid input.Try again...')
except:
    print('Try Again and Enter a proper Value ')