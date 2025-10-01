FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

temp=float(input("entrez la temperature :"))
scale=input("en celsius ou fahrenheit (C/F)").strip().upper()
if scale=="C":
    converted=convert_to_fahrenheit(temp)
    print("la temperature en fahren",converted)
elif scale=="F":
    converted=convert_to_celsius(temp)
    print("la temperature en celsius",converted)
else:
    print("Invalid temperature. Please enter a numeric value.")
    