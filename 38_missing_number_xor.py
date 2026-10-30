
def find_missing_number(numbers):
    n = len(numbers)

    result = n

    for i in range(n):
        result = result ^ i ^ numbers[i]

    return result


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("Missing number:", find_missing_number(numbers))
