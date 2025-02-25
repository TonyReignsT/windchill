# T = Air temperature in Fahrenheit and V = Wind speed in miles per hour
def get_windchill(T, V):
  wind_chill = 35.74 + 0.6215 * T - 35.75 * V ** 0.16 + 0.4275 * T * V ** 0.16
  return wind_chill


def convert_c_to_f(temp):
  return (temp * 9/5) + 32


temp = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius?(F / C): ").upper()

if unit == "C":
  # convert Celsius to Fahrenheit
  temp = convert_c_to_f(temp)
elif unit == "F":
  temp = temp
else:
  print("Invalid input. Please try again.")

for wind_speed in range(5, 65, 5):
  wind_chill = get_windchill(temp, wind_speed)
  print(f"At temperature {temp}F, and wind speed {wind_speed} mph, the wind chill is  {wind_chill:.2f}F")


# while True:
#   temp = float(input("What is the temperature? "))
#   unit = input("Fahrenheit or Celsius?(F / C): ").upper()

#   if unit == "C":
#     # convert Celsius to Fahrenheit
#     temp = (temp * 9/5) + 32
#   elif unit == "F":
#     temp = temp
#   else:
#     print("Invalid input. Please try again.")
#     continue

#   for wind_speed in range(5,65, 5):
#     wind_chill = get_windchill(temp, wind_speed)
#     print(f"At temperature {temp}F, and wind speed {wind_speed} mph, the wind chill is  {wind_chill:.2f}F")
  
#   break
