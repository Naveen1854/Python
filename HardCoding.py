#Remove Hard Coding
#Good Practice
def calculate_sum(x:int, y:int):
  """
  Returns the sum of two Numbers
  """
  return x+y

#Good Practice
total_sum=input('Enter value of Total Sum ')
bonus_points=input('Enter value of bonus_points ')
print(f'Data Type of total_sum is {type(total_sum)}and \n' +
      f'bonus_points is {type(bonus_points)}')
final_score=calculate_sum(total_sum, bonus_points)
print(f'Final Score is {final_score}')
