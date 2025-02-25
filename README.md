# Wind Chill Calculator

This project calculates the wind chill based on the air temperature and wind speed. The wind chill is the temperature it "feels like" outside and is based on the rate of heat loss from exposed skin caused by wind and cold.

## Files

- `windchill.py`: The main script that calculates and displays the wind chill.

## Functions

### `get_windchill(T, V)`

Calculates the wind chill based on the air temperature in Fahrenheit and wind speed in miles per hour.

- **Parameters:**
  - `T` (float): Air temperature in Fahrenheit.
  - `V` (float): Wind speed in miles per hour.

- **Returns:**
  - `wind_chill` (float): The calculated wind chill in Fahrenheit.

### `convert_c_to_f(temp)`

Converts a temperature from Celsius to Fahrenheit.

- **Parameters:**
  - `temp` (float): Temperature in Celsius.

- **Returns:**
  - `temp_f` (float): Temperature in Fahrenheit.

## Usage

1. Run the script `windchill.py`.
2. Enter the air temperature when prompted.
3. Enter the unit of the temperature (Fahrenheit or Celsius).
4. The script will display the wind chill for wind speeds ranging from 5 to 60 mph in increments of 5 mph.

## Example

```plaintext
What is the temperature? 30
Fahrenheit or Celsius?(F / C): F
At temperature 30.0F, and wind speed 5 mph, the wind chill is  25.27F
At temperature 30.0F, and wind speed 10 mph, the wind chill is  21.16F
At temperature 30.0F, and wind speed 15 mph, the wind chill is  18.54F
At temperature 30.0F, and wind speed 20 mph, the wind chill is  16.79F
At temperature 30.0F, and wind speed 25 mph, the wind chill is  15.47F
At temperature 30.0F, and wind speed 30 mph, the wind chill is  14.41F
At temperature 30.0F, and wind speed 35 mph, the wind chill is  13.54F
At temperature 30.0F, and wind speed 40 mph, the wind chill is  12.81F
At temperature 30.0F, and wind speed 45 mph, the wind chill is  12.19F
At temperature 30.0F, and wind speed 50 mph, the wind chill is  11.66F
At temperature 30.0F, and wind speed 55 mph, the wind chill is  11.19F
At temperature 30.0F, and wind speed 60 mph, the wind chill is  10.78F
