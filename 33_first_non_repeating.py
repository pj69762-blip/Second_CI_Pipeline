
def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char

    return None


if __name__ == "__main__":
    string = input("Enter a string: ")
    result = first_non_repeating(string)

    if result is None:
        print("No non-repeating character found")
    else:
        print("First non-repeating character:", result)
