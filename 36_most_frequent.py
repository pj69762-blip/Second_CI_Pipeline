
def most_frequent(numbers):
    if not numbers:
        return None

    frequency = {}

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())

    for num in numbers:
        if frequency[num] == max_count:
            return num


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    result = most_frequent(numbers)

    if result is None:
        print("The list is empty")
    else:
        print("Most frequent element:", result)
