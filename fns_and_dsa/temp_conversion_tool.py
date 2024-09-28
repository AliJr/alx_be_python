FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):   
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def main():
    current_temp=input("Enter the temperature to convert: ")
    temp_type=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if temp_type=="C":
        print(current_temp+"°C is",str(convert_to_fahrenheit(float(current_temp)))+"°F")
    elif temp_type=="F":
        print(current_temp+"°F is",str(convert_to_celsius(float(current_temp)))+"°C")
    else:
        print("Invalid input")
    
    
# Run the program
if __name__ == "__main__":
    main()