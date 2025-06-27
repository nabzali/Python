def count_characters(input_string):
    char_counts = {}
    for char in input_string:
        if char not in char_counts:
            char_counts[char] = 0
        else:
            char_counts[char] += 1
    return char_counts

# Example usage
user_input = input("Enter a string: ")
result = count_characters(user_input)
print(result)
