#Handling Type Conversion
#Good
def calculate_sum(x:int, y:int):
  """
  Returns the sum of two Numbers
  """
  return x+y

total_sum=int(input('Enter value of total_sum '))
bonus_points=int(input('Enter value of bonus_points '))
print(f'Data Type of total_sum is {type(total_sum)} and \n +'
      f'bonus_points is {type(bonus_points)}')
final_score=calculate_sum(total_sum , bonus_points)
print(f'Final score is {final_score}')