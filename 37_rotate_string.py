
def rotate_string(string, k):
    if not string:
        return string

    k = k % len(string)

    return string[-k:] + string[:-k] if k else string


if __name__ == "__main__":
    string = input("Enter a string: ")
    k = int(input("Enter number of positions to rotate: "))

    print("Rotated string:", rotate_string(string, k))
