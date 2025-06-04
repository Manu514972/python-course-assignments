import sys
from collections import Counter
import os

def count_digits_in_file(input_file, output_file='report.txt'):
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)

    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count digits
    digit_counts = Counter(char for char in content if char.isdigit())

    # Write report
    with open(output_file, 'w', encoding='utf-8') as f:
        for digit in map(str, range(10)):
            count = digit_counts.get(digit, 0)
            f.write(f"{digit}: {count}\n")

    print(f"Digit count written to '{output_file}'.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python count_digits_in_file.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    count_digits_in_file(input_file)
