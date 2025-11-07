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




Algorithm (Simple Steps)
1.	Input the text and pattern.
2.	Let n = length(text) and m = length(pattern).
3.	For each position i from 0 to n - m:
o	Compare pattern with text[i:i+m].
o	If they are the same → print or store index i.
4.	End.




