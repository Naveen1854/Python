# Temperature Conversion using match block
temperature_entered = input("Enter the Temperature: ")
if temperature_entered.isdigit():
  temperature = float(temperature_entered);
  unit = input("Enter the unit of temperature (C for celsius, F for Fahrenheit): ")
  match unit:
    case 'C' | 'c':
      celcius = temperature
      fahrenheit = (celcius * 9/5) + 32
      print(f'{celcius}°C is equal to {fahrenheit:.1f}°F')
    case 'F' | 'f':
      fahrenheit = temperature
      celcius = (fahrenheit -32) * 5/9
      print(f'{fahrenheit}°C is equal to {celcius:.1f}°C')
    case _:
       print(f"Invalid unit {unit}. please enter 'C' for celsius or 'F' for fahrenheit.")
else:
  print(f'Invalid Temperature {temperature_entered}. please enter digits.')