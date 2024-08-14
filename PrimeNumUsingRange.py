# Prime Numbers using for loop and range function
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
if start_range >= end_range:
    print(f'Invalid range, the end range must be greater than start range')
    exit()
prime_found = False
number = start_range
print(f'Prime number in the range {start_range:02d} to {end_range:02d}.')

for number in range(start_range, end_range + 1):
    if number > 1 :
        is_prime = True
        for devisor in range(2,int(number ** 0.5) + 1):
            if number % devisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_found = True
            print(number, end = " ")
if not prime_found:
    print("No prime found in a specified range.")