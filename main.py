def sort(width, height, length, mass):
    volume = width * height * length
    
    is_bulky = (volume >= 1000000) or (width >= 150) or (height >= 150) or (length >= 150)

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        stack = "REJECTED"
    elif is_bulky or is_heavy:
        stack = "SPECIAL"
    else:
        stack = "STANDARD"

    return stack

if __name__ == "__main__":
    print("Please enter the package dimensions and mass.")

    try:
        user_width = float(input("Enter width (cm): "))
        user_height = float(input("Enter height (cm): "))
        user_length = float(input("Enter length (cm): "))
        user_mass = float(input("Enter mass (kg): "))

        result_stack = sort(user_width, user_height, user_length, user_mass)

        print(f"Dimensions: {user_width}cm x {user_height}cm x {user_length}cm")
        print(f"Mass: {user_mass}kg")
        print(f"This package should go to the: {result_stack} stack.")

    except ValueError:
        print("\nInvalid input. Please enter numbers for dimensions and mass.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")