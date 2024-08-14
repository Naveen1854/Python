# Temperature Conversion using if block
temperature_entered = input("Enter the Temperature: ")
if temperature_entered.isdigit():
  temperature = float(temperature_entered);
  unit = input("Enter the unit of temperature (C for celsius, F for Faherenheit): ")
  if unit == 'C' or unit == 'c':
    converted_temp = (temperature * 9/5) + 32
    print(f'{temperature}°C is equal to {converted_temp:.1f}°F')
  elif unit == 'F' or unit == 'f':
    converted_temp = (temperature - 32) * 9/5
    print(f'{temperature}°F is equal to {converted_temp:.1f}°C')
  else:
    print(f"Invalid unit {unit}. please enter 'C' for Celsius or 'F' for fahrenheit.")
else:
  print(f"Invalid temperature {temperature_entered}. please enter digits.")
