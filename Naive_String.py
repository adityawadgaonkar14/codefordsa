
def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    indices = []  # create a list to store indices

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:   # correct slicing
            indices.append(i)          # correct way to append

    return indices


# Example usage
text = "ABCAABCCBA"
pattern = "ABC"
result = naive_string_match(text, pattern)
print("Pattern found at indices:", result)
