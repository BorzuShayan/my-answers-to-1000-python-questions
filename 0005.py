wind_speed = float(input(">> Enter wind speed: "))
temperature = float(input(">> Enter the temperature: "))

wind_chill = 13.12 + 0.6215 * temperature - 11.37 * (wind_speed ** 0.16) + 0.3965 * temperature * (wind_speed ** 0.16)

print(f">> The wind chill is: {wind_chill}")