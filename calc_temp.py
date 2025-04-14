#!/usr/bin/env python3
# Created By: Chanella
# Date: April 08, 2025
# Welcome to the temperature converter
# This program allows you to convert temperatures from celsius,fahrenheit and kelvin
# Please follow the instructions below to perform your conversion


def main():
    try:
        # asks the user to choose a conversion option
        print("Enter 1 to convert from celsius,2 from fahrenheit , 3 from kelvin")
        choice = int(input("Your choice :"))  # convert input to integer

        # convert from celsius
        if choice == 1:
            celsius = float(input("Enter the temperature in celsius"))
            fahrenheit == (celsius * 9 / 5) + 32  # convert to fahrenheit
            kelvin == celsius + 273.15  # convert to kelvin
            print("The temperature in fahrenheit is:", fahrenheit)
            print("The temperature in kelvin is:", kelvin)

        # convert from fahrenheit
        elif choice == 2:
            fahrenheit = float(input("Enter the temperature in fahrenheit"))
            celsius = (fahrenheit - 32) * 5 / 9  # convert to celsius
            kelvin = celsius + 273.15  # convert to kelvin
            print("The temperature in celsius is:", celsius)
            print("The temperature in kelvin is:", kelvin)
            # convert to kelvin
        elif choice == 3:
            kelvin = float(input("Enter the temperature in kelvin"))
            celsius = kelvin - 273.15  # convert to celsius
            fahrenheit = (celsius * 9 / 5) + 32  # convert to fahrenheit
            print("The temperature in celsius is:", celsius)
            print("The temperature in fahrenheit is:", fahrenheit)

        # check for invalid choices
        else:
            print("Invalid choice please enter 1,2 or 3")

    # check for input errors(non-numeric values )
    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
