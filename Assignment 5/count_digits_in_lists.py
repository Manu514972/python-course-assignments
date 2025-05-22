from collections import Counter

numbers = [1203, 1256, 312456, 98]

def count_digits(numbers):
   
    all_digits = ''.join(str(number) for number in numbers)

    digit_counts = Counter(all_digits)

    for digit in '0123456789':
        print(f"{digit}: {digit_counts.get(digit, 0)}")

if __name__ == "__main__":
    count_digits(numbers)
