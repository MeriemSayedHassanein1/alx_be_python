FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

try:
    temp = float(input("Enter the temperature: "))
    scale = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if scale == "C":
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted:.2f}°F")
    elif scale == "F":
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted:.2f}°C")
    else:
        print("Invalid scale. Please enter C or F.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
