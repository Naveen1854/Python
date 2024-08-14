#step-1
user_name=input('Enter User Name: ')
first_place=input('Enter the First Place you would like to visit: ')
second_place=input('Enter the Second Place you would like to visit: ')
third_place=input('Enter the Third Place you would like to visit: ')
year=input('Enter the Year you would like to visit: ')

#step-2
print(f'\n Hello {user_name} and places to visit are {first_place}',second_place, third_place,sep=',',end='')
print(f' in the year of {year}')