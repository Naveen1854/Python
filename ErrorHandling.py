#Handling User Error
#Good

def calculate_sum(x:int, y:int):
  """
  Returns the Sum of Two Numbers
  """
#Bad: Not Handling the exact error occured

try:
  total_sum=int(input('Enter value of total sum '))
  bonus_points=int(input('Enter value of bonus_points '))
  print(f'Data Type of total_sum is {type(total_sum)} and \n' +
        f'bonus_points is {type(bonus_points)}')
  final_score=calculate_sum(total_sum,bonus_points)
  print(f'Final score is {final_score}')
except:
    print('Try Again and Enter a proper value')