# Prime Numbers using Python
def is_prime(number):
    if number == 1 :
        return False
    for devisor in range(2, int(number ** 0.5) + 1):
        if number % devisor == 0:
            return False
    return True
# prompt user for input
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if start >= end:
    print("Invalid range. end of range must be greater than start. ")
    exit()
prime_numbers = []
for number in range(start, end + 1 ):
    is_prime(number) and prime_numbers.append(number)
if len(prime_numbers) > 0:
    print(f"Prime numbers in the range {start} to {end} are: {prime_numbers}")
else:
    print(f"No prime numbers found in the range {start} to {end}.")