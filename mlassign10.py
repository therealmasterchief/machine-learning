def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings


input_string =input("enter your string")
substrings = all_substrings(input_string)
print(substrings)