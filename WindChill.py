# Windchill program
month_entered = input("Enter the month number(1 to 12): ")
month = None
if month_entered.isdecimal() or month_entered.isdigit():
    month = int(month_entered)
if month is not None and month in [11, 12, 1, 2]:
    temperatuer_entered = input("Enter the temperature between -50 and 50 °F: ")
    wind_speed_entered = input("Enter the temperature between 3 and 120 mph: ")
    temperature = None
    if temperatuer_entered.isdecimal() or temperatuer_entered.isdigit():
        temperature = float(temperatuer_entered)
    wind_speed = None
    if wind_speed_entered.isdecimal() or wind_speed_entered.isdigit():
        wind_speed = float(wind_speed_entered)
    if temperature is None:
        print(f'Invalid input {temperatuer_entered}. Enter valid temperature')
    elif wind_speed is None:
        print(f'Invalid input {wind_speed_entered}. Enter valid wind speed')
    elif abs(temperature) > 50 or wind_speed < 3 or wind_speed > 120:
        print(f"Invalid input  Temperature {temperature} must be between -50",
              f"and 50 °F, and wind speed {wind_speed} between 3 and 120 mph.")
    else:
        wind_chill = (35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16))
        print(f"wind_chill: {wind_chill:.2f} °F for Month {month} with",
              f"temperature {temperature} and wind speed {wind_speed}")
else:
    print(f"wind chill computation is not applicable for month {month_entered}. ")