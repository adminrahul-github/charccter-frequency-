input_string = "mississippi"
freq = {}

for char in input_string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1


print("Per char frequency in '{}' is :\n {}".format(input_string, str(freq)))
