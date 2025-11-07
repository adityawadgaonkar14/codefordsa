# Naive String Matching Algorithm

def string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    # Loop through text till (n - m)
    for i in range(n - m + 1):
        match = True
        # Check each character of pattern
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)
    
    return positions


# -------- MAIN PROGRAM --------
text = input("Enter the text string: ")
pattern = input("Enter the pattern to find: ")

positions = string_matching(text, pattern)

if positions:
    print("Pattern found at indices:", positions)
else:
    print("Pattern not found in the text.")
