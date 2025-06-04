import sys
import os

def load_colors_from_file(filename):
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

    with open(filename, 'r', encoding='utf-8') as f:
        colors = [line.strip() for line in f if line.strip()]
    
    if not colors:
        print("Error: The file is empty or contains no valid colors.")
        sys.exit(1)

    return colors

def display_menu(colors):
    print("Please select a color from the list below:\n")
    for idx, color in enumerate(colors, start=1):
        print(f"{idx}. {color}")

def get_user_choice(colors):
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(colors):
                return colors[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python color_selector_file.py <colors_file.txt>")
        sys.exit(1)

    colors_file = sys.argv[1]
    colors = load_colors_from_file(colors_file)
    display_menu(colors)
    selected_color = get_user_choice(colors)
    print(f"\nYou selected: {selected_color}")

if __name__ == "__main__":
    main()
