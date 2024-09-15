#Task 1, 2, 3, 4

def convert_to_celsius():
    while True:
        try:
            temperature_f = float(input("Enter the temperature(Fahrenheit): ")) 
        except ValueError:
            print("The input should be a number")
        else:
            temperature_c = (temperature_f - 32) * 5/9
            print(f"{temperature_f} degrees in Celsius is: {temperature_c} degrees")
            break
        finally:
            print("Thank you for using the program!")


(convert_to_celsius())
