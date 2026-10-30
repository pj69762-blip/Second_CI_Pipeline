
def move_zeros(numbers):
    non_zero = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]

    return non_zero + zeros


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    result = move_zeros(numbers)

    print("List after moving zeros:", result)
