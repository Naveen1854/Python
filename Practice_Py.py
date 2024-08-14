#bad practice
x=10
y=20
z=x+y
print(f'The value z is {z}')

#Good practice
total_sum=10
bonus_points=20
final_score=total_sum + bonus_points
print(f'Final score is {final_score}')

#Good practice
#defining Function Block for add
def add(x,y):
  return x + y

total_sum=10
bonus_points=20
final_score=add(total_sum , bonus_points)
print(f'Final_score is {final_score}')