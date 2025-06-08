def get_input():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        return length, width
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_input()

def calculate_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def print_results(area, perimeter):
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

if __name__ == "__main__":
    length, width = get_input()
    area, perimeter = calculate_area_perimeter(length, width)
    print_results(area, perimeter)
