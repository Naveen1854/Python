import threading
#printing name of the main thread
print(f'Main or Default Thread Name is {str(threading.current_thread().name)}')
x=100
y=400
z=x+y
#print("The Result of adding", x ,"and", y, "is", z)
print(f"The Result of adding {x} and {y} is {z}")