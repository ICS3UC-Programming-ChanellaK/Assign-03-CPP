// copyright (c) 2025 Chanella rights reserved
// created by:chanella
//Created on:April 6,2025
// Welcome to the temperature converter
// This temperature allows you to convert temperatures from celsius ,fahrenheit and kelvin
// Please follow the instructions below to perform your conversion


#include <iostream>

int main() {
    int choice;
    float inputTemp;
    float celsius, fahrenheit, kelvin;

    std::cout << "Enter 1 to convert from celsius,\n";
    std::cout << "Enter 2 to convert from fahrenheit,\n";
    std::cout << "Enter 3 to convert from Kelvin:";
    std::cin >> choice;


    if (choice == 1) {
        std::cout << "Enter the temperature in Celsius:";
        std::cin >> inputTemp;

        celsius = inputTemp;
        fahrenheit = (celsius * 9 / 5) + 32;
        kelvin = celsius + 273.15;

    }  else if (choice == 2) {
          std::cout << "Enter the temperature in fahrenheit:";
          std::cin >> inputTemp;

          fahrenheit = inputTemp;
          celsius = (fahrenheit - 32) * 5 / 9;
          kelvin = celsius + 273.15;

    }  else if (choice == 3) {
        std::cout << "Enter the temperature in Kelvin:";
        std::cin >> inputTemp;

        kelvin = inputTemp;
        celsius = kelvin - 273.15;
        fahrenheit = (celsius * 9 / 5) + 32;

    } else {
        std::cout << "Invalid option selected." << std::endl;
        return 1;
    }

    std::cout << "Temperature in celsius:" << celsius << std::endl;
    std::cout << "Temperature in fahrenheit:"  << fahrenheit << std::endl;
    std::cout << "Temperature in Kelvin:" << kelvin << std::endl;

    return 0;
}
