# #Bad Practice
def calc(y):
  return total_sum + y

#Good practice
def calculate_sum(x:int, y:int):
    """
    Returns the sum of 2 Numbers
    """
    return x + y

#Good practice
total_sum=10
bonus_points=20
print(f'Data Type of total_sum is {type(total_sum)} and \n' +
      f'bonus_points is {type(bonus_points)}')
final_score=calculate_sum(total_sum, bonus_points)
print(f'Final_score is {final_score}')
#print(f'{type(total_sum)}')
# help(type)