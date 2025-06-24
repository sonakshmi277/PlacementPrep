s = "dhab"
ct = 0
last = -1  # last index where a, b, or c was found

for i in range(len(s)):
    if s[i] in {'a', 'b', 'c'}:
        last = i  # update the last valid position
    ct += last + 1  # add how many substrings ending at i have a/b/c

print(ct)
