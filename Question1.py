def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def convert_2_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def main():
    try:
        fahrenheit = get_number("Enter Fahrenheit temperature: ")
        celsius = convert_2_celsius(fahrenheit)

    except Exception as e:
        print(f"An error occurred: {e}")

    else:
        print(f"{fahrenheit} F is {celsius:.2f} C.")

    finally:
        print("Thank you for using my converter!")


if __name__ == "__main__":
    main()