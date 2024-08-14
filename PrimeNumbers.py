# Prime Numbers using while loop
# Step 1: prompt user for input
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
# Step 2: check if input is valid
if start_range >= end_range:
    print(f'Invalid range {start_range}and {end_range}.'
    "End of range must be greater than start. ")
    exit()
# Step 3: Initialize the number variable to start a flag to check if any
# prime number is found
prime_found = False
number = start_range

#print prime numbers within the range
print(f'Prime numbers in the range {start_range:02d} to {end_range:02d}:')

# Step 4: while loop to check the prime number with-in the range
while number >= start_range and number <= end_range:
    if number > 1:
        is_prime = True
        # Step 5: Nested for loop to check the variable number is a prime.
        #Logic used is starting from 2 till the sqrt of the variable number,
        # Check the modulus. If reminder is 0 the number is prime
        for devisor in range(2, int(number ** 0.5) + 1):
            if number % devisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_found = True
            print(number,end = " ")
    number = number + 1
# Step 6: If no prime numbers are found, print a message
    if not prime_found:
        print("No prime numbers found in the specified range.")