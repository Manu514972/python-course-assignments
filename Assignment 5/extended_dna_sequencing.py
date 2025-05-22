import re

def extract_and_sort_valid_segments(sequence):
    valid_segments = re.findall(r'[ACTG]+', sequence)

    sorted_segments = sorted(valid_segments, key=len, reverse=True)

    return sorted_segments

if __name__ == "__main__":
    try:
        user_input = input("Enter a DNA sequence: ")
        result = extract_and_sort_valid_segments(user_input.upper())
        print(result)
    except KeyboardInterrupt:
        print("\nInput cancelled.")
