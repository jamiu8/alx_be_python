
# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Ask user for input
        temp_str = input("Enter the temperature: ").strip()
        if not temp_str.replace(".", "", 1).isdigit() and not (
            temp_str.startswith("-") and temp_str[1:].replace(".", "", 1).isdigit()
        ):
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp = float(temp_str)
        unit = input("Is this in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if unit == "F":
            print(f"{temp}°F is {convert_to_celsius(temp):.2f}°C")
        elif unit == "C":
            print(f"{temp}°C is {convert_to_fahrenheit(temp):.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

