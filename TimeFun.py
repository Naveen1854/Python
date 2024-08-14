import time
x=100
y=100
z=x+y
start_time=time.time()
print("The Result of adding",x, "and",y,"is",z)
print("--- %s micro seconds ---"% ((time.time()-start_time)*10**6))

print(f"The Result of adding {x} and {y} is {z}")
print("--- %s micro seconds ---"% ((time.time()-start_time)*10**6))